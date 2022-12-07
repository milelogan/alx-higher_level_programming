#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return my_list

    new_list = [element if element is not search else replace for element in my_list]
    return new_list
