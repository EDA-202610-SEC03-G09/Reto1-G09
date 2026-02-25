def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist

def get_element(my_list, index):
    
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    my_list['elements'].insert(0, element)
    my_list['size'] += 1    
    return my_list

def add_last(my_list, element):    
    my_list['elements'].append(element)    
    my_list['size'] += 1    
    return my_list

def size(my_list):    
    return my_list["size"]
    
def first_element(my_list):   
    if my_list["size"] == 0:
        raise IndexError("list index out of range")    
    return my_list["elements"][0]

def is_empty(my_list):    
    return my_list["size"] == 0

def last_element(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    return my_list["elements"][my_list["size"] - 1]

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    my_list["elements"] = my_list["elements"][:pos] + my_list["elements"][pos+1:]
    my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    first_element = my_list["elements"][0]
    my_list["elements"] = my_list["elements"][1:]
    my_list["size"] -= 1
    return first_element

def remove_last(my_list):
    if my_list["size"] == 0:
        raise IndexError("list index out of range")
    last_element = my_list["elements"][my_list["size"] - 1]
    my_list["elements"] = my_list["elements"][:-1]
    my_list["size"] -= 1
    return last_element

def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list['size']:
        raise IndexError("La posición está fuera de rango")
    my_list['elements'] = my_list['elements'][:pos] + [element] + my_list['elements'][pos:]
    my_list['size'] += 1
    return my_list

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list['size']:
        raise IndexError("list index out of range")
    my_list['elements'][pos] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    if (pos_1 < 0 or pos_1 >= my_list['size']) or (pos_2 < 0 or pos_2 >= my_list['size']):
        raise IndexError("list index out of range")
    temp = my_list['elements'][pos_1]
    my_list['elements'][pos_1] = my_list['elements'][pos_2]
    my_list['elements'][pos_2] = temp
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= my_list['size']:
        raise IndexError("list index out of range")
    sub_elements = my_list['elements'][pos_i : pos_i + num_elements]
    new_list = {
        "size": len(sub_elements),
        "elements": sub_elements
    }
    
    return new_list
