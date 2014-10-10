class Linked_list:

    def __init__(self):
        tail = Node(None, None)
        self.head = tail
        self.length = 0

    def insert(self, val):
        new = Node(val, self.head)
        self.head = new
        self.length += 1

    def search(self, val):
        running = True
        current = self.head
        while running:
            if current.value == val:
                return current
            elif current.pointer is None:
                running = False
            else:
                current = current.pointer
        return None

    def size(self):
        return self.length

    def pop(self):
        final = self.head
        self.head = final.pointer
        self.length -= 1
        return final.value

    def remove(self, val):
        running = True
        current = self.head
        last = None
        while running:
            if current.value == val:
                last.pointer = current.pointer
                self.length -= 1
                running = False
            elif current.pointer is None:
                running = False
            else:
                last = current
                current = current.pointer
        return None

    def __str__(self):
        running = True
        current = self.head
        final = ()
        while running:
            if current.value:
                final += (current.value, )
                current = current.pointer
            else:
                running = False
        return str(final)


class Node:

    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer
