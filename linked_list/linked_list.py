class Node:

    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer


class Linked_list:

    def __init__(self):
        tail = Node(None, None)
        self.head = tail
        self.length = 0

    def insert(self, val):
        '''Inserts a new item at the head of the list'''
        new_node = Node(val, self.head)
        self.head = new_node
        self.length += 1

    def search(self, val):
        '''Returns the first node with the value passed in if it is in the list'''
        currently_selected = self.head
        while currently_selected.value is not None:
            if currently_selected.value == val:
                return currently_selected
            else:
                currently_selected = currently_selected.pointer
        return None

    def size(self):
        '''Returns the number of items in the list'''
        return self.length

    def pop(self):
        '''Returns and removes the head of the list'''
        if self.head.value is None:
            return None
        else:
            return_value = self.head
            self.head = return_value.pointer
            self.length -= 1
            return return_value.value

    def remove(self, val):
        '''Removes the first Node with a value matching the value passed in'''
        currently_selected = self.head
        previously_selected = None
        while currently_selected.value is not None:
            if currently_selected.value == val:
                if previously_selected is not None:
                    previously_selected.pointer = currently_selected.pointer
                else:
                    self.head = currently_selected.pointer
                self.length -= 1
                break
            else:
                previously_selected = currently_selected
                currently_selected = currently_selected.pointer

    def __str__(self):
        currently_selected = self.head
        linked_list_tuple = ()
        while currently_selected.value is not None:
            linked_list_tuple += (currently_selected.value, )
            currently_selected = currently_selected.pointer
        return str(linked_list_tuple)
