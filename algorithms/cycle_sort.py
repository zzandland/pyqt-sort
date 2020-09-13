from algorithms.iterator import Iterator
from typing import List, Tuple

class CycleSort(Iterator):

    def __init__(self, data: List[int]):
        super().__init__(data)
        self.i = self.j = 0
        self.k = self.i + 1
        self.found = False
        self.end = False
        self.seen = set()

    def getPointers(self) -> Tuple[int, int]:
        return (self.j, self.k)

    def hasNext(self) -> bool:
        return not self.end

    def next(self) -> List[int]:
        if self.found:
            self.seen.add(self.j)
            if self.j != self.i:
                self.data[self.i], self.data[self.j] = self.data[self.j], self.data[self.i]
            else:
                while self.i in self.seen:
                    self.i += 1
                    if self.i == len(self.data) - 1:
                        self.end = True
                        break
            self.found = False
            self.j = self.i
            self.k = self.i + 1
        else:
            if self.data[self.i] > self.data[self.k]: self.j += 1
            self.k += 1
            if self.k == len(self.data): self.found = True
        return self.data

class OptimizedCycleSort(Iterator):

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
        else:
            self.i += 1
        if self.i == len(self.data): self.end = True
        return self.data
