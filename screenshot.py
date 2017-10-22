#!/bin/python

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from base64 import standard_b64encode
from os import environ
import json

f = open("image.png", "rb") # open our image file as read only in binary mode
image_data = f.read()              # read in our image file

b64_image = standard_b64encode(image_data)

client_id = environ.get("IMGUR_CLIENT_ID")
headers = {'Authorization': 'Client-ID ' + client_id}

data = {'image': b64_image, 'title': 'test'} # create a dictionary.

request = Request(
    url="https://api.imgur.com/3/upload.json",
    data=urlencode(data).encode('utf-8'),
    headers=headers
)
response = urlopen(request).read()

parse = json.loads(response)
print(parse['data']['link'])
