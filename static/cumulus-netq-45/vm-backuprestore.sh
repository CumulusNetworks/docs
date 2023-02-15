#!/bin/bash
#Script release: NetQ v4.5
# Performs netq vm data backup and restore
# Run vm-backuprestore.sh for usage

#Globals
BACKUP_DIR="/opt/backuprestore"
NETQ_APP_RELEASE="/etc/app-release"
NETQ_APP_RELEASE_BACKUP="/tmp/app-release"
LOGFILE="/var/log/vm-backuprestore.log"
CONFIG_KEY_BACKUP='/tmp/config-key'
CASSANDRA_DATA_DIR="/mnt/cassandra/"
STATIC_POD_BACKUP_DIR="$BACKUP_DIR/static_manifests"
STATIC_POD_DIR="/etc/kubernetes/manifests"
PROMETHEUS_DATA_DIR="/mnt/prometheus/"
APP_SEARCH_DATA_DIR="/mnt/netq-app-search/"
LCM_DATA_DIR="/mnt/lcm/"
KAFKA_DATA_DIR="/mnt/kafka-broker/" 
ZOOKEEPER_DATA_DIR="/mnt/zookeeper/"
ZOOKEEPER_LOGS_DIR="/mnt/zookeeper-logs/"
CASSANDRA_CACHE_DIR='/mnt/cassandra/saved_caches/'
OPERATION=''
STANDALONE="standalone"
CLUSTER="cluster"
CLOUD="cloud"
ONPREM="onprem"
AGENT_CONFIG_MANUAL="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq-44/Installation-Management/Install-NetQ/Install-NetQ-Agents/#configure-netq-agents-using-a-configuration-file"

#######################################
# Method to log to console and file
# Globals:
#   LOGFILE
# Arguments:
#  Log statement
#######################################
_logmsg()
{
  echo -en "$(date +%c) - ${*} \n" | sudo tee -a $LOGFILE
}

#######################################
# Method to scale static pods
# Globals:
#   STATIC_POD_DIR
#   STATIC_POD_BACKUP_DIR
# Arguments:
#  Replica count
#######################################
_scale_static_pods(){
  local replica
  replica=$1
  _check_dir $STATIC_POD_DIR
  _check_dir $STATIC_POD_BACKUP_DIR
  _logmsg "Scaling static pods to replica $replica"
  if [ -n "$(ls $STATIC_POD_BACKUP_DIR)" ]; then
      cp "$STATIC_POD_BACKUP_DIR"/netq-app*  $STATIC_POD_DIR
    else
      _logfile "Directory is empty:  $STATIC_POD_BACKUP_DIR"
  fi
  if [ "$replica" -eq 0 ]; then
    if [ -n "$(ls $STATIC_POD_DIR/netq-app*)" ]; then
      cp "$STATIC_POD_DIR"/netq-app* $STATIC_POD_BACKUP_DIR
      rm "$STATIC_POD_DIR"/netq-app*
    else
      _logfile "Directory is empty:  $STATIC_POD_BACKUP_DIR"
    fi
  fi
}

#######################################
# Method to log to file
# Globals:
#   LOGFILE
# Arguments:
#  Log statement
#######################################
_logfile()
{
  echo -en "$(date +%c) - ${*} \n" >> $LOGFILE
}


#######################################
# Method to retry a command based on its output
# The method retries a command for a given number of time
# till the output of the command is empty
# Globals:
#   None
# Arguments:
#  Number of retry
#  Interval in seconds between each retry
#  Command to execute
#######################################
_retry()
{
local max_retry
local retry_interval
local cmd
max_retry=$1
retry_interval=$2
shift 2
read -r -a cmd <<< "$@"
n=0
until [ "$n" -ge "$max_retry" ]
  do
    success="true"
    if [[ -n $(bash -c "${cmd[*]}") ]]; then
      success="false"
      _logfile "Retry count: $n"
      n=$((n+1)) 
      _logfile "Sleeping for $retry_interval seconds"
      sleep "$retry_interval"
    else
      break
    fi
  done
  if [ "$success" == "false" ]; then
    echo "Retry of command ${cmd[*]} failed, the output is not empty."
    bash -c "${cmd[*]}"
    exit 1
  fi
}

#######################################
# Method to get namespaces based on cluster type
# Globals:
#  None
# Arguments:
#  None
#######################################
_namespaces(){
  local namespaces
  namespaces=("default" "ingress-nginx")
  if [  "$(_netq_install_type)" == "$ONPREM" ]; then
    namespaces+=("monitoring")
  fi
  echo "${namespaces[@]}"
}

#######################################
# Method to scale operators
# Globals:
#  None
# Arguments:
#  replicas
#######################################
_scale_operators(){
  local replicas
  replicas=$1
  operators=('kafka-operator' 'cassandra-operator' 'netq-apps-operator' 'netq-ui-operator' 'netq-ui' 'transport-operator' 'master-operator' 'netq-manifest-operator' 'netq-apps' 'netq-edge' 'netq-kafka' 'netq-central' 'netq-installer' 'netqapps'  'netqedge' 'netqkafka' 'netqcentral' 'netqclustermanager' 'netqinstaller' )
  for i in "${operators[@]}"; do
    if [ -n "$(kubectl get deployment "$i" -n default --ignore-not-found)" ]; then
      kubectl scale deployment "$i" -n default --replicas="$replicas"  > /dev/null 2>&1
    fi
  done
}

#######################################
# Method to set dirs to backup
#  None
# Arguments:
#  None
#######################################
_backup_dirs(){
  local dirs
  dirs=("$CASSANDRA_DATA_DIR")
  if [  "$(_netq_install_type)" == "$ONPREM" ]; then
    dirs+=("$PROMETHEUS_DATA_DIR" "$KAFKA_DATA_DIR"" $ZOOKEEPER_DATA_DIR" "$ZOOKEEPER_LOGS_DIR" "$APP_SEARCH_DATA_DIR" "$LCM_DATA_DIR")
  fi
   echo "${dirs[@]}"
}

#######################################
# Method to set files to backup
#  None
# Arguments:
#  None
#######################################
_backup_files(){
  local files
  files=("$NETQ_APP_RELEASE_BACKUP" "$CONFIG_KEY_BACKUP")
  echo "${files[@]}"
}

#######################################
# Method to scale daemonsets
# Globals:
#   None
# Arguments:
#   replica count
#######################################
_scale_daemonsets(){
  local replica
  local resource
  resource="daemonset"
  replica=$1
  _logmsg "Scaling all daemonsets to replica $replica"
  read -r -a ns <<< "$(_namespaces)"
  for ns in "${ns[@]}"; do
    if [ -z "$(kubectl get "$resource" -n "$ns" --ignore-not-found)" ]; then
      _logfile "No resource $resource found in namespace $ns"
      continue
    fi
    kubectl get "$resource" -n  "$ns" --no-headers --ignore-not-found|awk '{print $1}'| while read line ; do
      if [ "$replica" -eq 0 ]; then
        kubectl patch "$resource" "$line" -n "$ns"  -p '{"spec": {"template": {"spec": {"nodeSelector": {"non-existing": "true"}}}}}'  > /dev/null 2>&1
      else
        kubectl -n "$ns" patch "$resource" "$line" --type json -p='[{"op": "remove", "path": "/spec/template/spec/nodeSelector/non-existing"}]'  > /dev/null 2>&1
      fi
    done
  done
}

#######################################
# Method to scale cluster pods
# Globals:
#   None
# Arguments:
#   replica count
#######################################
_scale_pods()
{
  local replica=$1
  local ns
  _logmsg "Scaling all pods to replica $replica"
  read -r -a ns <<< "$(_namespaces)"
  local resources=("deployment" "sts" "rc")
  for ns in "${ns[@]}"; do
    for resource in  "${resources[@]}"; do
      if [ -z "$(kubectl get "$resource" -n "$ns" --ignore-not-found)" ]; then
        _logfile "No resource $resource found in namespace $ns"
        continue
      fi
      kubectl scale "$resource" -n "$ns"  --replicas="$replica" --all  > /dev/null 2>&1
    done
  done
}
#######################################
# Method to stop all pods in k8s cluster
# Globals:
#   None
# Arguments:
#   replica count
#######################################
stop_pods()
{
  local cmd
  local ns
  _scale_operators 0
  _scale_static_pods 0
  _scale_pods 0
  _scale_daemonsets 0
  _logmsg "Waiting for all pods to go down"
  read -r -a ns <<< "$(_namespaces)"
  for ns in "${ns[@]}"; do
    _logfile "Waiting for all pods to go down in namespace: $ns"
    cmd=("kubectl get pods -n $ns --no-headers --ignore-not-found")
    _retry 30 60 "${cmd[@]}"
  done
  _logmsg "All pods are down"
}

#######################################
# Method to start all pods in k8s cluster
# Globals:
#   None
# Arguments:
#   replica count
#######################################
start_pods()
{
  local cmd
  local ns
  _scale_operators 1
  _scale_static_pods 1
  _scale_pods 1
  _scale_daemonsets 1
  _logmsg "Waiting for all pods to come up"
  read -r -a ns <<< "$(_namespaces)"
  for ns in "${ns[@]}"; do
    _logfile "Waiting for all pods to come up in namespace: $ns"
     cmd=("kubectl get pods -n $ns --no-headers|grep -v Running")
    _retry 30 60 "${cmd[@]}"
  done
  _logmsg "All pods are up"
}

#######################################
# Method to exit if directory does not exist
# Globals:
#   None
# Arguments:
#   Directory name
#######################################
_check_dir()
{
  local directory=$1
  if [ ! -d "$directory" ];then
    _logmsg "Directory $directory does not exist"
    exit 1
  fi  
}
 
#######################################
# Method to exit if file does not exist
# Globals:
#   None
# Arguments:
#   File name
#######################################
_check_file()
{
  local filename=$1
  if [ ! -f "$filename" ];then
    _logmsg "File $filename does not exist"
    exit 1
  fi  
}
 
#######################################
# Method to parse from netq release file
# Globals:
#   OPERATION
#   NETQ_APP_RELEASE
#   NETQ_APP_RELEASE_BACKUP
# Arguments:
#   Key
#######################################
_parse_release_file(){
  if [ "$OPERATION" != "restore" ]; then
    cp $NETQ_APP_RELEASE  $NETQ_APP_RELEASE_BACKUP
  fi
  cat $NETQ_APP_RELEASE_BACKUP |grep  "$1"| cut -d "=" -f 2| xargs
}

#######################################
# Method to get netq version
# Globals:
#   None
# Arguments:
#   None
#######################################
_netq_version(){
  _parse_release_file "BOOTSTRAP_VERSION"
}

#######################################
# Method to get netq installation type
# Globals:
#   STANDALONE
#   CLUSTER
# Arguments:
#   None
#######################################
_netq_cluster_type(){
    if [ "$(kubectl get node|grep -c Ready)" == '1' ] ;then
      echo "$STANDALONE"
    else
      echo "$CLUSTER"
    fi
}

#######################################
# Method to set netq config key
# Globals:
#   CONFIG_KEY_BACKUP
# Arguments:
#   None
#######################################
_set_config_key(){
  cf=$(kubectl get cm netq-opta-configkey -o yaml|grep configkey:| cut -d ":" -f 2| xargs)
  echo "$cf" > $CONFIG_KEY_BACKUP
}

#######################################
# Method to get netq config key
# Globals:
#   CONFIG_KEY_BACKUP
# Arguments:
#   None
#######################################
_get_config_key(){
  _check_file $CONFIG_KEY_BACKUP
  cat $CONFIG_KEY_BACKUP 
}

#######################################
# Method to check if cloud or onprem
# Globals:
#   ONPREM
#   CLOUD
# Arguments:
#   None
#######################################
_netq_install_type(){
  if _parse_release_file "APPLIANCE_NAME"|grep "On-premises" > /dev/null ; then
    echo $ONPREM
  else
   echo $CLOUD
  fi
}

#######################################
# Method to get backup file name
# Globals:
#   BACKUP_DIR
# Arguments:
#   None
#######################################
_backup_file(){
    echo "$BACKUP_DIR/backup-netq-$(_netq_cluster_type)-$(_netq_install_type)-$(_netq_version)-$(date +%Y-%m-%d_%H_%M_%S_%Z).tar"
}

#######################################
# Method to backup vm data to a tarball
# Globals:
#   CASSANDRA_CACHE_DIR
# Arguments:
#   None
#######################################
backup()
{
  local dirs
  local backup_file
  _logmsg "Starting backup of data, the backup might take time based on the size of the data"
  stop_pods
  _set_config_key
  read -r -a dirs <<< "$(_backup_dirs)"
  for d in  "${dirs[@]}"; do
    _check_dir "$d"
  done
  read -r -a files <<< "$(_backup_files)"
  for f in  "${files[@]}"; do
    _check_file "$f"
  done
  backup_items=("${dirs[@]}" "${files[@]}")
  backup_file=$(_backup_file)
  _logmsg "Creating backup tar $backup_file"
  cmd=("sudo tar --exclude=$CASSANDRA_CACHE_DIR -cPf $backup_file ${backup_items[*]}")
  _retry 5 60 "${cmd[@]}"
  echo -e "Backup is successful, please scp it to the master node the below command:
      sudo scp $backup_file cumulus@<ip_addr>:/home/cumulus\n
  Restore the backup file using the below command:
      ./vm-backuprestore.sh --restore --backupfile $backup_file"
}

#######################################
# Method to restore vm data from tarball
# Globals:
#   BACKUP_FILE
# Arguments:
#   None
#######################################
restore()
{
  _logmsg "Starting restore of data"
  if [[ -z $BACKUP_FILE ]];then
      _logmsg "Please provide backup file name with --backupfile "
      exit 1
  fi
  _check_file "$BACKUP_FILE"
  _logmsg "Extracting release file from backup tar"
  tar -xPf "$BACKUP_FILE" "$NETQ_APP_RELEASE_BACKUP"
  _logmsg "Cleaning the system"
  read -r -a dirs <<< "$(_backup_dirs)"
  read -r -a files <<< "$(_backup_files)"
  backup_items=("${dirs[@]}" "${files[@]}")
  for f in  "${backup_items[@]}"; do
    rm -rf "$f"|| true
  done
  _logmsg "Restoring data from tarball $BACKUP_FILE"
  sudo tar -xPf "$BACKUP_FILE"
  sudo chown -R 100000:100000 /mnt
  echo -e "Data restored successfully
  Please follow the below instructions to bootstrap the cluster
  The config key restored is $(_get_config_key), alternately the config key is available in file $CONFIG_KEY_BACKUP\n
  Pass the config key while bootstrapping:
  Example(standalone): netq install standalone full interface eth0 bundle /mnt/installables/NetQ-4.5.0-SNAPSHOT.tgz config-key $(_get_config_key)
  Example(cluster):    netq install cluster full interface eth0 bundle /mnt/installables/NetQ-4.5.0-SNAPSHOT.tgz config-key $(_get_config_key)
  Alternately you can setup config-key post bootstrap in case you missed to pass it during bootstrap
  Example(standalone): netq install standalone activate-job config-key $(_get_config_key)
  Example(cluster):    netq install cluster activate-job config-key $(_get_config_key)
  In case the IP of the restore machine is different from the backup machine, please reconfigure the agents using: $AGENT_CONFIG_MANUAL"
}

#######################################
# Method to print usage
# Globals:
#  None
# Arguments:
#   None
#######################################
_print_usage()
{
    echo "NAME"
    echo "Script to backup and restore netq"
    echo "SYNOPSIS"
    echo "    $me  [--help|-h] [--backup|-b] [--restore|-r] [--backupfile|-f] [--stop_pods|-k] [--start_pods|-s]"
    echo "DESCRIPTION"
    echo "    --help        -h   prints help for script"
    echo "    --backup      -b   creates backup tarball from netq"
    echo "    --restore     -r   restores backup tarball to netq"
    echo "    --backupfile  -f   backup tarball file path to restore"
    echo "    --stop_pods   -k   stops all kubernetes pods in netq"
    echo "    --start_pods  -s   stops all kubernetes pods in netq"
}

#######################################
# Method to print user input
# Globals:
#  OPERATION
#  BACKUP_FILE
# Arguments:
#   Command line parameters
#######################################
_parse_input(){
  if [ $# -eq  0 ];then
    _print_usage
    exit 0
  fi
  while [[ $# -gt 0 ]];do
    key="$1"
    shift
    case $key in
      -h|--help)
      _print_usage
      ;;
      -b|--backup)
      export OPERATION="backup"
      ;;
      -r|--restore)
      export OPERATION="restore"
      ;;
      -k|--stop_pods)
      export OPERATION="stop_pods"
      ;;
      -s|--start_pods)
      export OPERATION="start_pods"
      ;;
      -f|--backupfile)
      export BACKUP_FILE="$1"
      shift
      ;;
      *)
      _logmsg "For supported options execute: vm-backuprestore.sh --help"
      exit 1
      ;;
  esac
  done
  _logmsg "Please find detailed logs at: $LOGFILE"
  $OPERATION
}

#######################################
# Main method
# Globals:
#  BACKUP_DIR
#  STATIC_POD_BACKUP_DIR
#  LOGFILE
# Arguments:
#   Command line parameters
#######################################
main(){
  sudo mkdir -p "$BACKUP_DIR"
  sudo mkdir -p "$STATIC_POD_BACKUP_DIR"
  if ! [ -f $LOGFILE ]; then
    sudo touch $LOGFILE
    sudo chmod ugo+w $LOGFILE
  fi
  _parse_input "$@"
}

# Entrypoint
main "$@"