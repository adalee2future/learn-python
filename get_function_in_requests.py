import requests

response = requests.get('http://placekitten.com/')

# Add your code below!
print response.status_code



################## Example response ##########################
# HTTP/1.1 200 OK
# Content-Type: text/xml; charset=UTF-8

# <?xml version="1.0" encoding="utf-8"?>
# <string xmlns="http://www.codecademy.com/">Accepted</string>
##############################################################

print response.headers