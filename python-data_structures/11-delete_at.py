#!/usr/bin/python3
def delete_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list[:]
    del new_list[idx]
    del my_list[idx]
    return new_list
