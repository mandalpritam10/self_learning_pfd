"""
Packages:
 are python functions that can be imported 
 in some other code file
"""

import json

def read_file(file_name):
    with open (file_name,"r") as file:
        return file.readlines()

def write_json(output_file,json_object):
    with open (output_file,"w+") as file:
        json.dump(json_object,file,indent=4)