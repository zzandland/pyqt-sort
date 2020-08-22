from algorithms.iterator import Iterator
from typing import List, Tuple

class BubbleSort(Iterator):

    def __init__(self, data: List[int]):
        self.data = data
        self.i = 1
        self.j = len(data)
        self.end = True

    def getPointers(self) -> Tuple[int, int]:
        return (self.i - 1, self.i)

    def hasNext(self) -> bool:
        return self.i < len(self.data)

    def next(self) -> List[int]:
        if self.data[self.i-1] > self.data[self.i]:
            self.data[self.i-1], self.data[self.i] = self.data[self.i], self.data[self.i-1]
            self.end = False
        self.i += 1
        if self.i == self.j and not self.end:
            self.i = 1
            self.j -= 1
            self.end = True
        return self.data
