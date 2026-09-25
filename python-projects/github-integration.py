# Program to demonstrate integration with Github to fetch the details
# of users who created Pull requests(Active) on Kubernetes Github repo

# First you need to install the request module before importing it
# by running: pip install requests
import requests

# URL to fetch Pull requests from the Github API
url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# Make a GET request to fetch pull requests data from the Github API
response = requests.get(url) # Add headers=headers inside get() for authentication

# Only if the response is successful
if response.status_code == 200:
    # Convert the JSON response into a dictionary
    pull_requests = response.json()

    # Create an empty dictionary to store PR creators and their counts
    pr_creators = {}

    # Iterate through each pull request and extract the creator's name
    for pull in pull_requests:
        creator = pull['user']['login']
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

    # Display the dictionary of PR creators and their counts
    print("PR Creators and Counts:")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count} PR(s)")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")



