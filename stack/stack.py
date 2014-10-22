class Node:

    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer


class Stack:

    def __init__(self):
        '''Creates an empty stack with an empty node to act as an endpoint'''
        tail = Node(None, None)
        self.head = tail

    def push(self, val):
        '''Adds one item to head of stack, points to previous head'''
        new_node = Node(val, self.head)
        self.head = new_node

    def pop(self):
        '''Removes head item and returns value, makes next item the new head'''
        if self.head.value is not None:
            return_item = self.head
            self.head = return_item.pointer
            return return_item.value
        else:
            return None

    def peek(self):
        '''Returns value of head item'''
        return self.head.value
