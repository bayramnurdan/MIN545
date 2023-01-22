# MIN 545 HW 6
# This code belongs to Nurdan Emin
# 2143139

import itertools


def post_from_pre(preorder):
    if not preorder:  # the list is empty
        return []
    else:
        root = preorder[0]
        left_child = list(itertools.takewhile(lambda x: x < root, preorder[1:]))  # create list of left child, by putting all the numbers smaller than root
        right_child = preorder[len(left_child) + 1:]  # the rest is right child
        return post_from_pre(left_child) + post_from_pre(right_child) + [root]  # recursive case
