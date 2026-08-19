class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = None(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node: Node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)

        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

        else:
            pass

    def _delete_recursive(self, current_node: Node, value):
        if current_node is None:
            return current_node

        if value < current_node.value:
            current_node.left = self._delete_recursive(current_node.left, value)

        elif value > current_node.value:
            current_node.right = self._delete_recursive(current_node.right, value)

        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            temp_node : Node = self._min_value_node(current_node.right)
            current_node.value = temp_node.value
            current_node.right = self._delete_recursive(current_node.right, temp_node.value)

        return current_node

    def _min_value_node(self, node : Node):
        current = node
        while current.left is not None:
            current = current.left
        return current




