def new_stack():
    stack = {
        'size': 0,
        'first': None,
        'last': None
    }
    return stack

def push(my_stack, element):
    
    nuevo_nodo = {
        'info': element,
        'next': None
    }
    
    if my_stack['size'] == 0:
        my_stack['first'] = nuevo_nodo
        my_stack['last'] = nuevo_nodo
    else:
        my_stack['last']['next'] = nuevo_nodo
        my_stack['last'] = nuevo_nodo
        
    my_stack['size'] += 1
    return my_stack

def pop(my_stack):
    if my_stack['size'] == 0:
        raise Exception('EmptyStructureError: stack is empty')
    if my_stack['size'] == 1:
        element = my_stack['first']['info']
        my_stack['first'] = None
        my_stack['last'] = None
        my_stack['size'] = 0
        return element
    current = my_stack['first']
    while current['next'] != my_stack['last']:
        current = current['next']
    
    element = my_stack['last']['info']  
    my_stack['last'] = current          
    current['next'] = None              
    my_stack['size'] -= 1

    return element

def is_empty(my_stack):
    return my_stack['size'] == 0

def top(my_stack):
    if my_stack['size'] == 0:
        raise Exception('EmptyStructureError: stack is empty')
    return my_stack['last']['info']

def size(my_stack):
    return my_stack['size']
