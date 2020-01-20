#!/usr/bin/env python3

import requests 
import json
import sys 

URL = "https://api.github.com/repos/cumulsunetworks/docs/"

if len(sys.argv) != 2:
    print("Github Auth token must be provided with no other arguments")
    exit(1)

token = sys.argv[1]

AUTH = {'Authorization': 'token ' + token}

def get_next_release():
    '''
    Gets the current release version from /docs and increments the patch version

    Returns a string of v<major_ver>.<minor_ver>.<patch_ver + 1>
    '''
    r = requests.get(URL + "releases/latest", AUTH)

    if not r.ok:
        print("Failed to get API response from latest release") 
        print("Response: {}".format(r.status_code))
        exit(1)
    
    try:
        doc_latest_release = str(r.json()["tag_name"])

        major_ver = doc_latest_release.split(".")[0]
        minor_ver = doc_latest_release.split(".")[1]
        patch_ver = int(doc_latest_release.split(".")[2])

        new_ver = patch_ver + 1

        new_ver = major_ver + "." + minor_ver + "." +  str(new_ver)
    except e:
        print("Failed to parse API reponse for releases. Error message: {} ".format(e))
        exit(1)
    
    return new_ver

def get_last_pr():
    '''
    Get the PR comments from the last merge to master
    '''

    r = requests.get(URL + "commits/HEAD", AUTH)
    
    if not r.ok:
        print("Failed to get API response from last commit to HEAD") 
        print("Response: {}".format(r.status_code))
        exit(1)

    return r.json()

def create_release(new_version, sha, message):
    '''
    Create a new release based on the generated version (tag_name).
    Use the most recent commit hash as the release to base it on.
    The body of the release will be the commit message of the PR.
    '''

    payload = dict()
    payload["tag_name"] = new_version
    payload["target_commitish"] = sha
    payload["name"] = "Cumulus Networks Docs " + new_version
    payload["body"] = message
    
    r = requests.post(URL + "releases", headers=AUTH, data=json.dumps(payload))

    if not r.ok:
        print("Failed to create release") 
        print("Response: {}".format(r.status_code))
        print(r.content)
        exit(1)
    

def main():
    version_string = get_next_release()
    pr_info = get_last_pr()

    pr_sha = pr_info["sha"]
    pr_message = pr_info["commit"]["message"]

    create_release(new_version=version_string, sha=pr_sha, message=pr_message )

    print("Release {} created successfully!".format(version_string))
    exit(0)

if __name__ == "__main__":
    main()