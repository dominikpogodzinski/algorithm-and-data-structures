class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.val:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def search(self, sought):
        if self.val == sought:
            return "I Found"
        if self.val > sought:
            if self.left is None:
                return "I`m not found"
            else:
                return self.left.search(sought)
        else:
            if self.right is None:
                return "I`m not found"
            else:
                return self.right.search(sought)

    def print_tree_pre_order(self):
        return None

    def print_tree_in_order(self):
        return None

    def print_tree_post_order(self):
        return None


if __name__ == "__main__":
    root = Node(13)
    root.insert(15)
    root.insert(4)
    root.insert(5)
    print(root.search(4))
    print(root.search(3))
    root.print_tree_post_order()
