#!/usr/bin/env python3

# Python 3.9.5

# 01_write_json_output_w_indentation.py

# Dependencies
import json
import os

path = "/Users/username/..."

# Generate data in the json format
request = {"name":"Abraxo", "item_number":"3748429", "product_category":"cleaning supplies"}

os.chdir(path)
filename = "output.json"

with open(filename, "w", encoding='utf-8') as outfile: 
    json.dump(request, outfile, ensure_ascii=False, indent=4)
