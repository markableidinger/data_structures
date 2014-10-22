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
        new = Node(val, self.head)
        self.head = new
        self.length += 1

    def search(self, val):
        '''Returns the first node with the value passed in if it is in the list'''
        current = self.head
        while current.value is not None:
            if current.value == val:
                return current
            else:
                current = current.pointer
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
        current = self.head
        last = None
        while current.value is not None:
            if current.value == val:
                if last is not None:
                    last.pointer = current.pointer
                else:
                    self.head = current.pointer
                self.length -= 1
                break
            else:
                last = current
                current = current.pointer

    def __str__(self):
        current = self.head
        linked_list_tuple = ()
        while current.value is not None:
            linked_list_tuple += (current.value, )
            current = current.pointer
        return str(linked_list_tuple)
