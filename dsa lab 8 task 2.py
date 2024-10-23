class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def set_value(self, value):
        self.value = value
    
    def set_left(self, left):
        self.left = left
    
    def set_right(self, right):
        self.right = right
    
    def get_value(self):
        return self.value
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.get_value():
            if node.get_left() is None:
                node.set_left(Node(value))
            else:
                self._insert_recursive(node.get_left(), value)
        else:
            if node.get_right() is None:
                node.set_right(Node(value))
            else:
                self._insert_recursive(node.get_right(), value)
    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        if node is None:
            return node
        
        if value < node.get_value():
            node.set_left(self._delete_recursive(node.get_left(), value))
        elif value > node.get_value():
            node.set_right(self._delete_recursive(node.get_right(), value))
        else:
            if node.get_left() is None:
                return node.get_right()
            elif node.get_right() is None:
                return node.get_left()
            
            temp = self._find_min(node.get_right())
            node.set_value(temp.get_value())
            node.set_right(self._delete_recursive(node.get_right(), temp.get_value()))
        
        return node
    
    def _find_min(self, node):
        current = node
        while current.get_left() is not None:
            current = current.get_left()
        return current
    
    def display_pre_order(self):
        self._pre_order_recursive(self.root)
    
    def _pre_order_recursive(self, node):
        if node:
            print(node.get_value(), end=" ")
            self._pre_order_recursive(node.get_left())
            self._pre_order_recursive(node.get_right())
    
    def display_in_order(self):
        self._in_order_recursive(self.root)
    
    def _in_order_recursive(self, node):
        if node:
            self._in_order_recursive(node.get_left())
            print(node.get_value(), end=" ")
            self._in_order_recursive(node.get_right())
    
    def display_post_order(self):
        self._post_order_recursive(self.root)
    
    def _post_order_recursive(self, node):
        if node:
            self._post_order_recursive(node.get_left())
            self._post_order_recursive(node.get_right())
            print(node.get_value(), end=" ")
    
    def total_elements(self):
        return self._count_elements(self.root)
    
    def _count_elements(self, node):
        if node is None:
            return 0
        return 1 + self._count_elements(node.get_left()) + self._count_elements(node.get_right())
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder traversal:")
bst.display_in_order()
print("\nTotal elements:", bst.total_elements())

bst.delete(30)
print("\nAfter deleting 30:")
bst.display_in_order()
print("\nTotal elements:", bst.total_elements())
