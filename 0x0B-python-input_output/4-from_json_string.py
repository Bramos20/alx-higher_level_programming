#!/usr/bin/python3
import json

def from_json_string(my_str):
    """
    Returns a Python data structure represented by a JSON string.

    :param my_str: The JSON string to be parsed.
    :return: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
