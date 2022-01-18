from avl import AVL
from bst import BST


class Node:
    def __init__(self, num):
        self.value = num
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    if node is None:
        return 0
    else:
        return node.height


def preorder(tree, root="first"):
    if root is None:
        return
    if root == "first":
        root = tree.root
    print(root.value)
    preorder(0, root.left)
    preorder(0, root.right)


def inorder(tree, root="first"):
    if root is None:
        return
    if root == "first":
        root = tree.root
    inorder(0, root.left)
    print(root.value)
    inorder(0, root.right)


def find(tree, val, node="first"):
    if node == "first":
        node = tree.root
    if node is None:
        return False
    elif val < node.value:
        return find(0, val, node.left)
    elif val > node.value:
        return find(0, val, node.right)
    else:
        return True


def insert_avl(binary_strings, dim):
    avl_tree = AVL()
    for string in binary_strings:
        # add value to tree and change to decimal integer
        if dim < 5:
            # convert to unsigned int 16 bit and inset tree
            avl_tree.insert(convert_str_to_uint16(string))
        elif dim == 5:
            # convert to unsigned int 32 bit and inset tree
            avl_tree.insert(convert32(string))
        elif dim > 5:
            # convert to unsigned int 64 bit and inset tree
            avl_tree.insert(convert64(string))
    return avl_tree


def insert_bst(binary_strings, dim):
    bst_tree = BST()
    for string in binary_strings:
        # add value to tree and change to decimal integer
        if dim < 5:
            # convert to unsigned int 16 bit and inset tree
            bst_tree.insert(convert_str_to_uint16(string))
        elif dim == 5:
            # convert to unsigned int 32 bit and inset tree
            bst_tree.insert(convert32(string))
        elif dim > 5:
            # convert to unsigned int 64 bit and inset tree
            bst_tree.insert(convert64(string))
    return bst_tree


def convert_str_to_uint16(bin_str):
    intt16 = int(bin_str, 2)
    # convert to unsigned-16 bit
    return intt16 % 2 ** 16


def convert32(bin_str):
    int32 = int(bin_str, 2)
    # convert to unsigned-32 bit
    return int32 % 2 ** 32


def convert64(bin_str):
    int64 = int(bin_str, 2)
    # convert to unsigned-32 bit
    return int64 % 2 ** 64