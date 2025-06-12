#!/usr/bin/python3
"""Define a function that converts a JSON string to an object."""
import json


def from_json_string(my_str):
    """Returns the object represented by a JSON string."""
    return json.loads(my_str)
