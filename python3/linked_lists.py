"""
Clean linked list implementation.
"""
from dataclasses import dataclass


@dataclass
class Node:
    val: str
    nxt = None

    def __str__(self):
        chars = [self.val]
        curr = self.nxt
        while curr is not None:
            chars.append(curr.val)
            curr = curr.nxt
        return ''.join(chars)


def list_to_ll(lst):
    root = Node(lst[0])
    curr = root
    for char in lst[1:]:
        curr.nxt = Node(char)
        curr = curr.nxt
    return root


def reverse(root):
    if root.nxt is None:
        return root
    last, curr, nxt = None, root, root.nxt
    while curr is not None:
        curr.nxt = last
        last = curr
        curr = nxt
        if curr is not None:
            nxt = curr.nxt
    return last


if __name__ == '__main__':
    lst = list_to_ll('hello')
    print(lst)
    lst = reverse(lst)
    print(lst)
