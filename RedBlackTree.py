from typing import Any, Type


class RedBlackTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value: Any) -> None:
        if self.root is None:
            self.root = RedBlackTreeNode(self)
            self.root.insert(value)
        else:
            self.root.insert(value)
        self.size += 1

    def print_in_order(self) -> None:
        if self.root is not None:
            self.root.print_in_order()

    def print_tree_size(self) -> None:
        print(f'Tree size is {self.size} nodes. ')

    def print_tree_height(self) -> None:
        print(f'Tree height is {self.root.calculate_height()}')

    def print_black_height(self):
        self.root.print_black_height()

    def get_all_elements(self) -> Any:
        return self.root.get_all_elements()

    def search_tree(self, value: Any) -> Type:
        return self.root.search_tree(value)


class RedBlackTreeNode:
    left: Type
    right: Type
    parent: Type

    def __init__(self, parent_tree: RedBlackTree, value=None):
        self.value = value
        self.tree = parent_tree
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'r'

    def search_tree(self, value: Any) -> Type:
        if self.value == value:
            return self
        elif self.value > value:
            if self.left is not None:
                return self.left.search_tree(value)
            else:
                return None
        elif self.value < value:
            if self.right is not None:
                return self.right.search_tree(value)
            else:
                return None

    def print_in_order(self) -> None:
        if self.left is not None:
            self.left.print_in_order()
        print(str(self.value) + "\n", end=" ")
        if self.right is not None:
            self.right.print_in_order()

    def insert(self, value: Any) -> None:
        if self.value is None:
            self.value = value

        elif value < self.value:
            if self.left is None:
                self.left = RedBlackTreeNode(self.tree, value)
                self.left.parent = self
                rb_fixup(self.left)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = RedBlackTreeNode(self.tree, value)
                self.right.parent = self
                rb_fixup(self.right)
            else:
                self.right.insert(value)

    def calculate_height(self) -> int:
        if self.left is None:
            left_height = 0
        else:
            left_height = self.left.calculate_height()

        if self.right is None:
            right_height = 0
        else:
            right_height = self.right.calculate_height()

        return 1 + max(left_height, right_height)

    def print_black_height(self) -> None:
        black_height = 0
        node = self
        while node is not None:
            if node.color == 'b':
                black_height += 1
            node = node.left
        print('black height is ' + str(black_height))

    def get_all_elements(self):
        left_list, right_list = [], []
        if self.left is not None:
            left_list = self.left.get_all_elements()
        if self.right is not None:
            right_list = self.right.get_all_elements()
        return left_list + [self.value] + right_list


def left_rotate(x: RedBlackTreeNode) -> None:
    y = x.right
    x.right = y.left
    if y.left is not None:
        y.left.parent = x
    y.parent = x.parent
    if x.parent is None:
        x.tree.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y


def right_rotate(y: RedBlackTreeNode) -> None:
    x = y.left
    y.left = x.right
    if x.right is not None:
        x.right.parent = y
    x.parent = y.parent
    if y.parent is None:
        y.tree.root = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
    x.right = y
    y.parent = x


def rb_fixup(z: RedBlackTreeNode) -> None:
    while z.parent is not None and z.parent != z.tree.root and z.parent.color == 'r':
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y is not None and y.color == 'r':
                y.color = 'b'
                z.parent.color = 'b'
                z.parent.parent.color = 'r'
                z = z.parent.parent

            elif z == z.parent.right:
                z = z.parent
                left_rotate(z)
            else:
                z.parent.color = 'b'
                z.parent.parent.color = 'r'
                right_rotate(z.parent.parent)

        elif z.parent == z.parent.parent.right:
            y = z.parent.parent.left
            if y is not None and y.color == 'r':
                y.color = 'b'
                z.parent.color = 'b'
                z.parent.parent.color = 'r'
                z = z.parent.parent

            elif z == z.parent.left:
                z = z.parent
                right_rotate(z)
            else:
                z.parent.color = 'b'
                z.parent.parent.color = 'r'
                left_rotate(z.parent.parent)

    z.tree.root.color = 'b'


if __name__ == '__main__':
    tree = RedBlackTree()
    for i in range(10, 15):
        tree.insert(i)
    for i in range(5, 0, -1):
        tree.insert(i)

    found_node = tree.root.search_tree(1)
    if found_node is not None:
        print("Found:", found_node.value)
    else:
        print("Not Found")

    tree.print_in_order()

    tree.print_black_height()
