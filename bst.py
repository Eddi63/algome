import Global_funcs_Trees


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val, root):
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
        return root
