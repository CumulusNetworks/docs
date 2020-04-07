#!/bin/sh
# Inspired by  https://gist.github.com/willprice/e07efd73fb7f13f917ea

echo "making local_clone directory" 
mkdir local_clone
git clone https://plumbis:${GH_TOKEN}@github.com/CumulusNetworks/docs.git local_clone


echo "moving into directory"
cd local_clone
pwd

echo "running git config"
git config --global user.email "docs@cumulusnetworks.com"
git config --global user.name "Cumulus Docs CI"

git checkout stage 

echo "running rn script"
echo ""
python3 utils/build_rns.py 

echo "running FOSS script"
echo ""
python3 utils/build_foss_licenses.py

sleep 1

git add *
git commit -m "Auto commit of release note update" -m "[skip ci]"
git push

exit $?