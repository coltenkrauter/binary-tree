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

    def __str__(self):
        in_order = ', '.join([f'{ i }' for i in self.in_order(self.root)])
        pre_order = ', '.join([f'{ i }' for i in self.pre_order(self.root)])
        post_order = ', '.join([f'{ i }' for i in self.post_order(self.root)])

        return ( 
            f'Root: { self.root.get() }\n'
            f'In-order: { in_order }\n'
            f'Pre-order: { pre_order }\n'
            f'Post-order: { post_order }\n'
        )
        

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

    def pre_order(self, root):
        res = []
        if root:
            res = [root.value]
            res += self.pre_order(root.left)
            res += self.pre_order(root.right)
        return res

    def in_order(self, root):
        res = []
        if root:
            res = self.in_order(root.left)
            res.append(root.value)
            res += self.in_order(root.right)
        return res

    def post_order(self, root):
        res = []
        if root:
            res = self.post_order(root.left)
            res += self.post_order(root.right)
            res.append(root.value)
        return res


tree = BinaryTree()
tree.insert(7)
tree.insert(2)
tree.insert(3)
tree.insert(5)
tree.insert(13)
tree.insert(523)
tree.insert(6)
tree.insert(31)
tree.insert(52)
tree.insert(17)

print(tree)