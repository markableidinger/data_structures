class Node:

    def __init__(self, value, previous, next):
        self.value = value
        self.previous = previous
        self.next = next


class Doubly_linked_list:

    def __init__(self):
        self.tail = Node(None, None, None)
        self.head = Node(None, None, self.tail)
        self.tail.previous = self.head

    def insert(self, val):
        new = Node(val, self.head, self.head.next)
        self.head.next.previous = new
        self.head.next = new

    def append(self, val):
        new = Node(val, self.tail.previous, self.tail)
        self.tail.previous.next = new
        self.tail.previous = new

    def pop(self):
        if self.head.next.value is None:
            return None
        else:
            return_value = self.head.next
            self.head.next = return_value.next
            return_value.next.previous = self.head
            return return_value.value

    def shift(self):
        if self.tail.previous.value is None:
            return None
        else:
            return_value = self.tail.previous
            self.tail.previous = return_value.previous
            return_value.previous.next = self.tail
            return return_value.value

    def remove(self, val):
        current = self.head.next
        last = self.head
        while current.value is not None:
            if current.value == val:
                last.next = current.next
                current.next.previous = last
                break
            else:
                last = current
                current = current.next
