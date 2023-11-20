#!/usr/bin/env python3

import os
from PIL import Image

img_dir = "supplier-data/images/"

new_size = (600, 400)
new_format = ".jpeg"

for img in os.listdir(img_dir):
    if img.endswith(".tiff"):
        old_img = Image.open(img_dir + img)
        new_img = old_img.resize(new_size).convert("RGB")
        img, e = os.path.splitext(img)
        outfile = img_dir + img + new_format
        new_img.save(outfile)