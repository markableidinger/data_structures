class Queue:

    def __init__(self):
        self.head = None
        self.end = None

    def enqueue(self, value):
        if self.head is None:
            new = Node(value, None)
            self.head = new
            self.end = new
        else:
            new = Node(value, None)
            self.end.next = new
            self.end = new

    def dequeue(self):
        if self.head is None:
            return None
        else:
            final = self.head.value
            self.head = self.head.next
            return final

    def peek(self):
        return self.head.value


class Node:

    def __init__(self, value, next):
        self.value = value
        self.next = next
