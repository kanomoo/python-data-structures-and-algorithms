# #  https://share.gemini.google/68l68tkQ4gyZ
# #  https://share.gemini.google/buHkJaab2mpf

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
    
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
    
#     def insert(self, value):
#         if self.root is None: self.root = Node(value)
#         else: self._insert_recursive(self.root, value)

#     def _insert_recursive(self, current_node: Node, value):
#         if value < current_node.value:
#             if current_node.left is None:
#                 current_node.left = Node(value)
#             else:
#                 self._insert_recursive(current_node.left, value)
#         elif value > current_node.value:
#             if current_node.right is None:
#                 current_node.right = Node(value)
#             else:
#                 self._insert_recursive(current_node.right, value)
#         else:
#             pass

#     def delete(self, value):
#         self.root = self._delete_recursive(self.root, value)
    
#     def _delete_recursive(self, current_node: Node, value):
#         if current_node is None:
#             return current_node
        
#         if value < current_node.value:
#             current_node.left = self._delete_recursive(current_node.left, value)
#         elif value > current_node.value:
#             current_node.right = self._delete_recursive(current_node.right, value)
#         else:
#             if current_node.left is None:
#                 return current_node.right
#             elif current_node.right is None:
#                 return current_node.left
        
#             temp_node: Node = self._min_value_node(current_node.right)
#             current_node.value = temp_node.value
#             current_node.right = self._delete_recursive(current_node.right, temp_node.value)
        
#         return current_node

#     def _min_value_node(self, current_node: Node) -> Node:
#         if current_node.left is None:
#             return current_node
#         return self._min_value_node(current_node.left)
    
# def print_pre_order(root: Node):
#     if root is not None:
#         print(root.value, end = "")
#         print_pre_order(root.left)
#         print_pre_order(root.right)

# if __name__ == "__main__":
#     tree = BinarySearchTree()
#     tree.insert(6)
#     tree.insert(2)
#     tree.insert(8)
#     tree.insert(1)
#     tree.insert(4)
#     tree.insert(3)
#     tree.delete(4)
#     print_pre_order(tree.root)




# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
    
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
    
#     def insert(self, value):
#         if self.root is None: self.root = Node(value)
#         else: self._insert_recursive(self.root, value)
    
#     def _insert_recursive(self, current_node: Node, value):
#         if value < current_node.value:
#             if current_node.left is None: current_node.left = Node(value)
#             else: self._insert_recursive(current_node.left, value)
#         elif value > current_node.value:
#             if current_node.right is None: current_node.right = Node(value)
#             else: self._insert_recursive(current_node.right, value)
#         else: pass
    
#     def delete(self, value):
#         self.root = self._delete_recursive(self.root, value)
    
#     def _delete_recursive(self, current_node: Node, value):
#         if current_node is None: return current_node

#         if value < current_node.value: current_node.left = self._delete_recursive(current_node.left, value)
#         elif value > current_node.value: current_node.right = self._delete_recursive(current_node.right, value)
#         else:
#             if current_node.left is None: return current_node.right
#             elif current_node.right is None: return current_node.left

#             temp_node: Node = self._min_value_node(current_node.right)
#             current_node.value = temp_node.value
#             current_node.right = self._delete_recursive(current_node.right, temp_node.value)

#         return current_node
    
#     def _min_value_node(self, current_node: Node) -> Node:
#         if current_node.left is None: return current_node
#         return self._min_value_node(current_node.left)
    
# def preOrder(root: Node):
#     if root is not None:
#         print(root.value, end = "")
#         preOrder(root.left)
#         preOrder(root.right)

# if __name__ == "__main__":
#     tree =  BinarySearchTree()
#     tree.insert(6)
#     tree.insert(2)
#     tree.insert(8)
#     tree.insert(1)
#     tree.insert(4)
#     tree.insert(3)
#     tree.delete(4)
#     preOrder(tree.root)


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
    

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
    
#     def insert(self, value):
#         if self.root is None: self.root = Node(value)
#         else: self._insert_recursive(self.root, value)
    
#     def _insert_recursive(self, current_node: Node, value):
#         if value < current_node.value:
#             if current_node.left is None: current_node.left = Node(value)
#             else: self._insert_recursive(current_node.left, value)
#         elif value > current_node.value:
#             if current_node.right is None: current_node.right = Node(value)
#             else: self._insert_recursive(current_node.right, value)
#         else: pass
    
#     def delete(self, value):
#         self.root = self._delete_recursive(self.root, value)
    
#     def _delete_recursive(self, current_node: Node, value):
#         if current_node is None: return current_node
#         if value < current_node.value: current_node.left = self._delete_recursive(current_node.left, value)
#         elif value > current_node.value: current_node.right = self._delete_recursive(current_node.right, value)
#         else:
#             if current_node.left is None: return current_node.right
#             elif current_node.right is None: return current_node.left

#             temp = self._min_value_node(current_node.right)
#             current_node.value = temp.value
#             current_node.right = self._delete_recursive(current_node.right, temp.value)

#         return current_node

#     def _min_value_node(self, current_node: Node):
#         if current_node.left is None : return current_node
#         return self._min_value_node(current_node.left)

# def preOrder(root: Node):
#     if root is not None:
#         print(root.value, end = "")
#         preOrder(root.left)
#         preOrder(root.right)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None: self.root = Node(value)
        else: self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, current_node: Node, value):
        if value < current_node.value:
            if current_node.left is None: current_node.left = Node(value)
            else: self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None: current_node.right = Node(value)
            else: self._insert_recursive(current_node.right, value)
        else: pass

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, current_node: Node, value):
        if current_node is None: return current_node
        if value < current_node.value: current_node.left = self._delete_recursive(current_node.left, value)
        elif value > current_node.value: current_node.right = self._delete_recursive(current_node.right, value)
        else:
            if current_node.left is None: return current_node.right
            elif current_node.right is None: return current_node.left

            temp: Node = self._min_node_value(current_node.right)
            current_node.value = temp.value
            current_node.right = self._delete_recursive(current_node.right, temp.value)
            
        return current_node
    
    def _min_node_value(self, current_node: Node):
        if current_node.left is None: return current_node
        else: return self._min_node_value(current_node.left)


    def preOrder(self):
        self._preOrder_recursive(self.root)
        print()
    
    def _preOrder_recursive(self, node: Node):
        if node is not None:
            print(node.value, end = "")
            self._preOrder_recursive(node.left)
            self._preOrder_recursive(node.right)

if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(6)
    tree.insert(7)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    tree.insert(2)
    tree.insert(1)


    tree.delete(4)
    tree.preOrder()
