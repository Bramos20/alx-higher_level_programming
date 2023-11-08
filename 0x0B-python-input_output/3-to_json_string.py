#!/usr/bin/python3
import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    :param my_obj: The object to be serialized to JSON.
    :return: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
