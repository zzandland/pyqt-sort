from algorithms.iterator import Iterator
from typing import List, Tuple

class SelectionSort(Iterator):

    def __init__(self, data: List[int]):
        super().__init__(data)
        self.i = self.j = self.mn = 0
        self.end = False

    def getPointers(self) -> Tuple[int, int]:
        return (self.i, self.mn)

    def hasNext(self) -> bool:
        return not self.end

    def next(self) -> List[int]:
        if self.data[self.i] < self.data[self.mn]: self.mn = self.i
        self.i += 1
        if self.i == len(self.data):
            self.data[self.mn], self.data[self.j] = self.data[self.j], self.data[self.mn]
            self.j += 1
            self.i = self.mn = self.j
        if self.j == len(self.data): self.end = True
        return self.data
