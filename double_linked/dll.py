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
            return_item = self.head.next
            self.head.next = return_item.next
            return_item.next.previous = self.head
            return return_item.value

    def shift(self):
        if self.tail.previous.value is None:
            return None
        else:
            return_item = self.tail.previous
            self.tail.previous = return_item.previous
            return_item.previous.next = self.tail
            return return_item.value

    def remove(self, val):
        currently_selected = self.head.next
        previously_selected = self.head
        while currently_selected.value is not None:
            if currently_selected.value == val:
                previously_selected.next = currently_selected.next
                currently_selected.next.previous = previously_selected
                break
            else:
                previously_selected = currently_selected
                currently_selected = currently_selected.next
