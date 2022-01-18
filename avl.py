import Global_funcs_Trees


class AVL:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Global_funcs_Trees.Node(val)
        else:
            self.root = self.insert_recursive(val, self.root)

    def insert_recursive(self, val, root):
        if root is None:
            return Global_funcs_Trees.Node(val)
        if val <= root.value:
            root.left = self.insert_recursive(val, root.left)
        elif val > root.value:
            root.right = self.insert_recursive(val, root.right)
        root.height = 1 + max(Global_funcs_Trees.height(root.left), Global_funcs_Trees.height(root.right))
        root = self.make_balanced(root, val)

        return root

    def make_balanced(self, root, val):
        balance = self.is_node_balanced(root)
        if balance > 1 and root.left.value > val:
            return self.rotateR(root)
        if balance < -1 and val > root.right.value:
            return self.rotateL(root)
        if balance > 1 and val > root.left.value:
            root.left = self.rotateL(root.left)
            return self.rotateR(root)
        if balance < -1 and val < root.right.value:
            root.right = self.rotateR(root.right)
            return self.rotateL(root)
        return root

    def is_node_balanced(self, node):
        if node is None:
            return 0
        else:
            return Global_funcs_Trees.height(node.left) - Global_funcs_Trees.height(node.right)

    def rotateR(self, node):
        a = node.left
        b = a.right
        a.right = node
        node.left = b
        node.height = 1 + max(Global_funcs_Trees.height(node.left), Global_funcs_Trees.height(node.right))
        a.height = 1 + max(Global_funcs_Trees.height(a.left), Global_funcs_Trees.height(a.right))
        return a

    def rotateL(self, node):
        a = node.right
        b = a.left
        a.left = node
        node.right = b
        node.height = 1 + max(Global_funcs_Trees.height(node.left), Global_funcs_Trees.height(node.right))
        a.height = 1 + max(Global_funcs_Trees.height(a.left), Global_funcs_Trees.height(a.right))
        return a
