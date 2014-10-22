class Priorityq:

    def __init__(self):
        self.contents = [None]

    def find_parent(self, index):
        if index <= 1:
            return None
        else:
            return self.contents[index // 2]

    def find_children(self, index):
        size = len(self.contents)
        if size >= index * 2 + 2:
            return (self.contents[index * 2], self.contents[(index * 2) + 1])
        elif size >= index * 2 + 1:

            return (self.contents[index * 2], None)
        else:
            return (None, None)

    def swap(self, index1, index2):
        temp = self.contents[index1]
        self.contents[index1] = self.contents[index2]
        self.contents[index2] = temp

    def find_greater_child(self, index):
        children = self.find_children(index)
        if children == (None, None):
            return None
        elif children[1] is None:
            return (children[0], 0)
        elif children[0][0] > children[1][0]:
            return (children[0], 0)
        else:
            return (children[1], 1)

    def top_down_sort(self):
        size = len(self.contents)
        current_index = 1
        if size <= 2:
            return
        else:
            while current_index * 2 + 1 <= size:
                greater_child, left_right = self.find_greater_child(current_index)
                if self.contents[current_index][0] < greater_child[0]:
                    self.swap(current_index, (current_index * 2) + left_right)
                    current_index = (current_index * 2) + left_right
                else:
                    return

    def bottom_up_sort(self, index):
        while index > 1:
            if self.contents[index][0] > self.find_parent(index)[0]:
                self.swap(index, index // 2)
                index = index // 2
            else:
                return

    def push(self, priority, value):
        if 0 <= priority <= 10:
            self.contents.append((priority, value))
            self.bottom_up_sort(len(self.contents) - 1)
        else:
            print('Priority must be a number from 0 to 10. Try again.')

    def pop(self):
        if len(self.contents) >= 2:
            returned_value = self.contents[1]
            self.contents[1] = self.contents[-1]
            del(self.contents[-1])
            self.top_down_sort()
            return returned_value
        else:
            return None

    def peek(self):
        if len(self.contents) > 1:
            return self.contents[1]
        else:
            return None

    def populate(self, iter):
        for el in iter:
            self.push(el[0], el[1])
