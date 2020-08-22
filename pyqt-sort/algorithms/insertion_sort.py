from algorithms.iterator import Iterator
from typing import List, Tuple

class InsertionSort(Iterator):

    def __init__(self, data: List[int]):
        super().__init__(data)
        self.i, self.j = 1, 0
        self.end = False

    def getPointers(self) -> Tuple[int, int]:
        return (self.i, self.j)

    def hasNext(self) -> bool:
        return not self.end

    def next(self) -> List[int]:
        if self.data[self.i] < self.data[self.j]:
            self.data[self.i], self.data[self.j] = self.data[self.j], self.data[self.i]
        self.j += 1
        if self.j == self.i: self.j, self.i = 0, self.i + 1
        if self.i == len(self.data): self.end = True
        return self.data
