#!/usr/bin/python3
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_items_to_list(args):
    try:
        # Load existing list from add_item.json
        existing_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        # If the file doesn't exist, create an empty list
        existing_list = []

    # Append new items from command line arguments to the list
    existing_list.extend(args[1:])

    # Save the updated list to add_item.json
    save_to_json_file(existing_list, 'add_item.json')

if __name__ == "__main__":
    add_items_to_list(sys.argv)
