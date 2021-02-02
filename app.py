'''

Binary Tree: In computer science, a binary tree is a tree data structure in which each 
node has at most two children, which are referred to as the left child 
and the right child.

Binary Search Tree: In computer science, a binary search tree, also called an ordered or sorted 
binary tree, is a rooted binary tree whose internal nodes each store a key 
greater than all the keys in the node's left subtree and less than those in 
its right subtree.

Following are the basic operations of a tree,
- Search: Searches an element in a tree.
- Insert: Inserts an element in a tree.
- Pre-order Traversal: Traverses a tree in a pre-order manner.
- In-order Traversal: Traverses a tree in an in-order manner.
- Post-order Traversal: Traverses a tree in a post-order manner.

'''

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def get(self):
        return self.value

    def set(self, value):
        self.value = value

    def get_children(self):
        children = []
        if self.left:
            children.append(self.left)
        if self.right:
            children.append(self.right)

        return children


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_node(self.root, value)

    def insert_node(self, node, value):
        if value < node.get():
            if node.left:
                self.insert_node(node.left, value)
            else:
                node.left = Node(value)
        elif value > node.get():
            if node.right:
                self.insert_node(node.right, value)
            else:
                node.right = Node(value)
        elif value == node.get():
            raise Exception('Unable to add nodes with duplicate values')
        else:
            raise Exception(f'Unable to determine where to insert { value } beneath node { node.get() }')

    def search(self, value):
        pass

    def pre_order(self):
        pass

    def in_order(self):
        pass

    def post_order(self):
        pass


tree = BinaryTree()
