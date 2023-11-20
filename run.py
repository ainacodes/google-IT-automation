#! /usr/bin/env python3

import os
import requests
import json

desc_dir = "supplier-data/descriptions/"
url = "http://localhost/fruits/"

for description in os.listdir(desc_dir):
    if description.endswith(".txt"):
        with open(desc_dir + description, 'r') as f:
            fruit_name = os.path.splitext(description)[0]
            data = f.read().split("\n")

            fruit_dict = {"name" :  data[0], "weight": int(data[1].strip(" lbs")), "description": data[2], "image_name": fruit_name + ".jpeg"}
            
            response = requests.post(url, json = fruit_dict)
            response.raise_for_status()
            print(response.request.url)
            print(response.status_code)
    