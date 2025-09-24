import requests
import os
from akamai.edgegrid import EdgeGridAuth
import json

# ANSI escape codes for colors and styles
RED = "\033[31m"
GREEN = "\033[32m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Environment setup
network_environment = os.getenv('AKAMAI_NETWORK_ENVIRONMENT', 'staging')
tags_to_invalidate = os.getenv('AKAMAI_TAGS_TO_INVALIDATE', 'tag1,tag2,tag3').split(',')
action = os.getenv('AKAMAI_ACTION', 'invalidate')  # Can be 'invalidate' or 'delete'

# Load Akamai credentials from environment variables
akamai_hostname = os.getenv('AKAMAI_HOST')
client_token = os.getenv('AKAMAI_CLIENT_TOKEN')
client_secret = os.getenv('AKAMAI_CLIENT_SECRET')
access_token = os.getenv('AKAMAI_ACCESS_TOKEN')

# Validate that all required credentials are present
required_vars = {
    'AKAMAI_HOST': akamai_hostname,
    'AKAMAI_CLIENT_TOKEN': client_token,
    'AKAMAI_CLIENT_SECRET': client_secret,
    'AKAMAI_ACCESS_TOKEN': access_token
}

missing_vars = [var for var, value in required_vars.items() if not value]
if missing_vars:
    print(f"{RED}Error: Missing required environment variables: {', '.join(missing_vars)}{RESET}")
    exit(1)

# EdgeGrid authentication setup
session = requests.Session()
session.auth = EdgeGridAuth(
    client_token=client_token,
    client_secret=client_secret,
    access_token=access_token
)

# Constructing the request URL
url = f"https://{akamai_hostname}/ccu/v3/{action}/tag/{network_environment}"

# Request headers and payload
headers = {"accept": "application/json", "content-type": "application/json"}
payload = {"objects": tags_to_invalidate}

# Making the POST request
response = session.post(url, headers=headers, json=payload)

# Processing the response
if response.status_code == 200 or response.status_code == 201:
    response_data = response.json()
    print(BOLD + "Cache invalidated successfully for the following tags:" + RESET)
    for tag in tags_to_invalidate:
        print(f"- {tag}")
    print(BOLD + "\nResponse from Akamai:" + RESET)
    # Print httpStatus and detail in green, and network_environment after detail
    print(f"{BOLD}{GREEN}httpStatus: {response_data.get('httpStatus')}{RESET}")
    print(f"{BOLD}{GREEN}detail: {response_data.get('detail')}{RESET}")
    print(f"{BOLD}network: {network_environment}{RESET}")  # Added network environment here
    print(f"{BOLD}purgeType: {action}")
    # Print additional details in default color (still bold)
    for key in ['supportId', 'purgeId', 'estimatedSeconds']:
        if key in response_data:
            print(f"{BOLD}{key}: {response_data.get(key)}{RESET}")
else:
    print(f"{RED}Failed to invalidate cache. Status code: {response.status_code}{RESET}")
    print(BOLD + response.text + RESET)