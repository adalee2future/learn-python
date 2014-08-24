import requests # this package I download from git hub, see requests in git projects

# Make a GET request here and assign the result to kittens:
kittens = requests.get("http://placekitten.com")

print kittens.text[559:1000]