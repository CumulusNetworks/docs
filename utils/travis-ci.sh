#!/bin/sh
# Credit: https://gist.github.com/willprice/e07efd73fb7f13f917ea

build_release_notes() {
  git checkout plumbis-stage travis-docs
  cd travis-docs
  # Current month and year, e.g: Apr 2018
  dateAndMonth=`date "+%b %Y"`
  # run the python script to pull new RNs
  python3 utils/build_rns.py
  # Stage the modified files in dist/output
  git add *
  # Create a new commit with a custom build message
  # with "[skip ci]" to avoid a build loop
  # and Travis build number for reference
  git commit -m "Auto commit of release note update on $dateAndMonth" -m "[skip ci]"
}

commit_release_notes() {
  # Remove existing "origin"
  git remote rm origin
  # Add new "origin" with access token in the git URL for authentication
  git remote add origin https://plumbis:${GH_TOKEN}@github.com/CumulusNetworks/docs.git > /dev/null 2>&1
  git push origin plumbis-stage --quiet > /dev/null 2>&1
}

pwd 

echo "making local_clone directory"
mkdir local_clone

echo "cloning..."
git clone https://plumbis:${GH_TOKEN}@github.com/CumulusNetworks/docs.git local_clone


echo "moving into directory"
cd local_clone
pwd

echo "running git config"
git config --global user.email "docs@cumulusnetworks.com"
git config --global user.name "Cumulus Docs CI"

echo "running rn script"
python3 utils/build_rns.py

git add *

# Attempt to commit to git only if "git commit" succeeded
if [ $? -eq 0 ]; then
  echo "Release note script detected release note updates. Commiting"
  dateAndMonth=`date "+%b %Y"`
  git commit -m "Auto commit of release note update on $dateAndMonth" -m "[skip ci]"
  git push
  exit $?
else
  echo "No release note updates."
  exit 0
fi