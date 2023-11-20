#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
img_dir = "supplier-data/images/"

for image in os.listdir(img_dir):
  if image.endswith(".jpeg"):
    with open(img_dir + image, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
