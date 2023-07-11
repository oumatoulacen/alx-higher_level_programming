#!/usr/bin/python3
'''Write a script that adds all arguments to a Python list,
and then save them to a file'''


import sys
'''os module'''


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
'''save to json file module'''


load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
'''load from json file module'''


try:
    existing_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    existing_list = []

new_items = sys.argv[1:]
existing_list.extend(new_items)

save_to_json_file(existing_list, "add_item.json")
