#!/bin/sh
# Credit: https://gist.github.com/willprice/e07efd73fb7f13f917ea

setup_git() {
  git config --global user.email "docs@cumulusnetworks.com"
  git config --global user.name "Cumulus Docs CI"
}

build_release_notes() {
  git checkout stage
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
  git remote add origin https://plumbis:${GH_TOKEN}@https://github.com/CumulusNetworks/docs.git > /dev/null 2>&1
  git push origin stage --quiet > /dev/null 2>&1
}

setup_git

build_release_notes

# Attempt to commit to git only if "git commit" succeeded
if [ $? -eq 0 ]; then
  echo "Release note script detected release note updates. Commiting"
  commit_release_notes
else
  echo "No release note updates."
fi