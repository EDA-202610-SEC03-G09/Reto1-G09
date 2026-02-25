from itertools import count




def new_list():
    newlist={
        "first": None,
        "last": None,
        "size": 0
    }
    return newlist

def get_element(my_list, pos):
    searchpos= 0
    node = my_list['first']
    while searchpos < pos:
        node = node['next']
        searchpos += 1
    return node['info']

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list['first']
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp['info']) == 0:
            is_in_array = True
        else:
            temp = temp['next']
            count += 1
            
    if not is_in_array:
        count = -1
    
    return count

def add_first(my_list, element):
    
    new_node = {
        "info": element,
        "next": my_list["first"]
    }


    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        my_list["first"] = new_node

    my_list["size"] += 1

    return my_list

def add_last(my_list, element):
    new_node = {
        "info": element,
        "next": None
    }

    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        my_list["last"]["next"] = new_node
        my_list["last"] = new_node

    my_list["size"] += 1

    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list["first"]["info"]

def is_empty(my_list):
    if my_list['size'] == 0:
        return True
    else:
        return False
    
def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    return my_list["last"]["info"]

def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    if pos == 0:
        my_list["first"] = my_list["first"]["next"]
    else:
        searchpos = 0
        node = my_list["first"]
        while searchpos < pos - 1:
            node = node["next"]
            searchpos += 1
        node["next"] = node["next"]["next"]
        if pos == size(my_list) - 1:
            my_list["last"] = node
    my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    removed = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1
    if my_list["size"] == 0:
        my_list["last"] = None
    return removed

def remove_last(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    removed = my_list["last"]["info"]
    if my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
    else:
        searchpos = 0
        node = my_list["first"]
        while searchpos < size(my_list) - 2:
            node = node["next"]
            searchpos += 1
        node["next"] = None
        my_list["last"] = node
    my_list["size"] -= 1
    return removed

def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')

    if pos == 0:
        return add_first(my_list, element)

    if pos == size(my_list):
        return add_last(my_list, element)

    new_node = {
        "info": element,
        "next": None
    }

    current = my_list["first"]
    for _ in range(pos - 1):
        current = current["next"]

    new_node["next"] = current["next"]
    current["next"] = new_node
    my_list["size"] += 1

    return my_list
    
def change_info(my_list, pos, element):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')

    node = my_list['first']
    for _ in range(pos):
        node = node['next']

    node['info'] = element

    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 >= size(my_list) or pos2 < 0 or pos2 >= size(my_list):
        raise Exception('IndexError: list index out of range')

    node1 = my_list['first']
    for _ in range(pos1):
        node1 = node1['next']

    node2 = my_list['first']
    for _ in range(pos2):
        node2 = node2['next']

    node1['info'], node2['info'] = node2['info'], node1['info']

    return my_list

def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= size(my_list) or num_elements < 0 or pos + num_elements > size(my_list):
        raise Exception('IndexError: list index out of range')

    sublist = new_list()
    current = my_list['first']
    for _ in range(pos):
        current = current['next']

    for _ in range(num_elements):
        add_last(sublist, current['info'])
        current = current['next']

    return sublist