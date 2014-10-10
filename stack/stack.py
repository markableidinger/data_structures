class Stack:

    def __init__(self):
        tail = Node(None, None)
        self.head = tail

    def push(self, val):
        new = Node(val, self.head)
        self.head = new

    def pop(self):
        final = self.head
        self.head = final.pointer
        return final.value

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
