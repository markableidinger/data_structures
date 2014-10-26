class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Binary_Tree():

    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while True:
                if value == current.value:
                    return
                elif value > current.value:
                    if current.right is None:
                        current.right = Node(value)
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        current.left = Node(value)
                    else:
                        current = current.left

    def locate(self, value):
        current = self.head
        parent = None
        while current is not None:
            if current.value == value:
                return (current, parent)
            elif value > current.value:
                parent = current
                current = current.right
            else:
                parent = current
                current = current.left
        return (None, None)

    def contains(self, value):
        if self.locate(value) == (None, None):
            return False
        return True

    def delete(self, value):
        location, parent = self.locate(value)
        if location is None:
            print('no such value')
            return
        if location.left is None and location.right is not None:
            location.value = location.right.value
            location.left = location.right.left
            location.right = location.right.right
        elif location.right is None and location.left is not None:
            location.value = location.left.value
            location.left = location.left.left
            location.right = location.left.right
        elif location.right is None and location.left is None:
            if parent is None:
                self.head = None
            elif parent.left == location:
                parent.left = None
            else:
                parent.right = None
        else:
            selected = location.left
            parent = None
            while selected.right is not None:
                parent = selected
                selected = selected.right
            if parent is not None:
                parent.right = None
            else:
                location.left = None
            location.value = selected.value

    def populate(self, iter):
        for el in iter:
            self.insert(el)

    def pre_order(self, node):
        if node is None:
            return
        pointer = node
        yield pointer.value
        if pointer.left is not None:
            for left_val in self.pre_order(pointer.left):
                yield left_val
        if pointer.right is not None:
            for right_val in self.pre_order(pointer.right):
                yield right_val

    def in_order(self, node):
        if node is None:
            return
        pointer = node
        if pointer.left is not None:
            for left_val in self.in_order(pointer.left):
                yield left_val
        yield pointer.value
        if pointer.right is not None:
            for right_val in self.in_order(pointer.right):
                yield right_val

    def post_order(self, node):
        if node is None:
            return
        pointer = node
        if pointer.left is not None:
            for left_val in self.post_order(pointer.left):
                yield left_val
        if pointer.right is not None:
            for right_val in self.post_order(pointer.right):
                yield right_val
        yield pointer.value

    def listify_pre(self):
        return list(self.pre_order(self.head))

    def listify_in(self):
        return list(self.in_order(self.head))

    def listify_post(self):
        return list(self.post_order(self.head))

    def breadth_first(self, node):
        queue = [node]
        output = []
        if node is None:
            return output
        while len(queue) > 0:
            pointer = queue.pop(0)
            output.append(pointer.value)
            if pointer.left is not None:
                queue.append(pointer.left)
            if pointer.right is not None:
                queue.append(pointer.right)
        return output

    def size(self):
        return len(self.breadth_first(self.head))

    def depth(self, node):
        if self.head is None:
            return 0
        if node.left is not None:
            left_depth = self.depth(node.left) + 1
        else:
            left_depth = 1
        if node.right is not None:
            right_depth = self.depth(node.right) + 1
        else:
            right_depth = 1
        return max(left_depth, right_depth)

    def balance(self):
        if self.head is None:
            return 0
        return (len(self.breadth_first(self.head.left)) - len(self.breadth_first(self.head.right)))
