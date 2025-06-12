#!/usr/bin/python3
"""Define a function that converts an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object."""
    return json.dumps(my_obj)
