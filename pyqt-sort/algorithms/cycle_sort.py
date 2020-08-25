from algorithms.iterator import Iterator
from typing import List, Tuple

class CycleSort(Iterator):

    def __init__(self, data: List[int]):
        super().__init__(data)
        self.i = 0
        self.end = False

    def getPointers(self) -> Tuple[int, int]:
        return (self.i, -1)

    def hasNext(self) -> bool:
        return not self.end

    def next(self) -> List[int]:
        val = self.data[self.i]
        if val != self.i + 1:
            self.data[self.i], self.data[val-1] = self.data[val-1], self.data[self.i]
        else: self.i += 1
        if self.i == len(self.data): self.end = True
        return self.data
