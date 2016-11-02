#!/usr/bin/python
# -*- coding: <encoding name> -*-

# tree node


class node(object):
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

    def set_left(self, left):
        left.parent = self
        self.left = left
        return self

    def set_right(self, right):
        right.parent = self
        self.right = right
        return self

    def set_parent(self, parent):
        self.parent = parent
        return self

    def __str__(self):
        return str(self.val)

root = node(1).set_left(node(2).set_right(node(4))).set_right(node(3).set_left(node(5).set_left(node(6)).set_right(node(7))))


def preorder(root):
    if root:
        print root,
        preorder(root.left)
        preorder(root.right)

preorder(root)
print


def inorder(root):
    if root:
        inorder(root.left)
        print root,
        inorder(root.right)
inorder(root)
print


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print root,

postorder(root)

print


def count_nodenum(root):
    if not root:
        return 0
    return 1 + count_nodenum(root.left) + count_nodenum(root.right)

print count_nodenum(root)

import os
