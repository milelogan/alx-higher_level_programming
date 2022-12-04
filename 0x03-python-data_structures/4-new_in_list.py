#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list_created = my_list.copy()
    if idx < 0:
        return new_list_created
    elif idx > len(my_list) - 1:
        return new_list_created
    else:
        new_list_created[idx] = element
        return new_list_created
