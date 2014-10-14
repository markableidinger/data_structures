class Queue:

    def __init__(self):
        self.contents = None
        self.head = None

    def enqueue(self, value):
        if self.contents is None:
            empty = True
        else:
            empty = False
        self.contents = (value, self.contents)
        if empty:
            self.head = self.contents

    def peek(self):
        return self.head[0]

    def dequeue(self):
        if self.contents is None:
            return None
        searching = True
        x = self.contents
        while searching:
            print x
            if x[1] is None:
                final = x[0]
                x = None
                print self.contents
                return final
            else:
                x = x[1]
