class Node:

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Queue:

    def __init__(self):
        self.head = None
        self.end = None

    def enqueue(self, value):
        '''adds a value to the end of the queue'''
        if self.head is None:
            new_node = Node(value, None)
            self.head = new_node
            self.end = new_node
        else:
            new_node = Node(value, None)
            self.end.next = new_node
            self.end = new_node

    def dequeue(self):
        '''returns and removes the value at the head of the queue'''
        if self.head is None:
            return None
        else:
            final = self.head.value
            self.head = self.head.next
            return final

    def peek(self):
        '''returns but does not remove the value at the head of the queue'''
        if self.head is None:
            print('Queue is empty')
            return None
        else:
            return self.head.value
