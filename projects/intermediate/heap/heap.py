class Heap:
    """
    Implements a Max-heap

    >>> h = Heap([1, 3, 4])
    >>> h.get_max()
    4
    """

    def __init__(self, numbers: list) -> None:
        self._internal = numbers[::]
        self.size = len(numbers)

        for i in reversed(range(self.size)):  #  from size-1 down to 0
            self._heapify(i)


    def _heapify(self, node):
        """
        Sorts the numbers according to the max-heap structure
        """
        if not self.is_leaf(node):
            max_child = self.left(node)

            if self.exists(self.right(node)):
                if self._internal[self.right(node)] > self._internal[max_child]:
                    max_child = self.right(node)

                if self._internal[max_child] > self._internal[node]:
                    self._internal[node], self._internal[max_child] = self._internal[max_child], self._internal[node]

            self._heapify(max_child)

    
    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        if index == 0:
            return 2  # Otherwise we would incorrectly identify the root as the right child
        return 2 * index

    def is_leaf(self, index: int):
        return index >= self.size // 2

    def exists(self, index):
        return 0 <= index <= self.size
    
    def get_max(self):
        return self._internal[0]

    def __repr__(self) -> str:
        return repr(self._internal)



if __name__ == "__main__":
    import doctest
    doctest.testmod()