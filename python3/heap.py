"""
Clean solution of heap data struction.
"""
import random


class Heap:

    def __init__(self):
        self.heap = []

    @property
    def size(self):
        return len(self.heap)

    def push(self, elem: int):
        idx = self.size
        self.heap.append(elem)
        # Bubble up.
        while idx > 0 and elem < self.heap[self._parent(idx)]:
            pidx = self._parent(idx)
            self.heap[idx], self.heap[pidx] = self.heap[pidx], self.heap[idx]
            idx = pidx

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        to_return = self.heap.pop()
        # Bubble down.
        if self.size:
            elem = self.heap[0]
            idx = 0
            while idx < self.size:
                lidx, ridx = self._lchild(idx), self._rchild(idx)
                to_swap = None
                if lidx < self.size and self.heap[lidx] < elem:
                    if ridx < self.size and self.heap[ridx] < elem:
                        if self.heap[lidx] < self.heap[ridx]:
                            to_swap = lidx
                        else:
                            to_swap = ridx
                    else:
                        to_swap = lidx
                elif ridx < self.size and self.heap[ridx] < elem:
                    to_swap = ridx
                if to_swap is None:
                    break
                self.heap[idx], self.heap[to_swap] = self.heap[to_swap], self.heap[idx]
                idx = to_swap
        return to_return

    def _parent(self, idx):
        return (idx - 1) // 2

    def _lchild(self, idx):
        return 2 * idx + 1

    def _rchild(self, idx):
        return 2 * idx + 2


def create_list(size, lower, upper):
    return [random.randint(lower, upper) for _ in range(size)]


if __name__ == '__main__':
    heap = Heap()
    test_list = create_list(25, 0, 10)
    for tl in test_list:
        heap.push(tl)
    print(test_list)
    print([heap.pop() for _ in range(heap.size)])
