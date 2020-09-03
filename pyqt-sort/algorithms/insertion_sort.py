from algorithms.iterator import Iterator
from typing import List, Tuple

class InsertionSort(Iterator):

    def __init__(self, data: List[int]):
        super().__init__(data)
        self.i, self.j = 1, 0
        self.stop = False
        self.end = False

    def getPointers(self) -> Tuple[int, int]:
        return (self.i, self.j)

    def hasNext(self) -> bool:
        return not self.end

    def next(self) -> List[int]:
        if self.data[self.j] > self.data[self.j+1]:
            self.data[self.j], self.data[self.j+1] = self.data[self.j+1], self.data[self.j]
            self.j -= 1
            if self.j == -1: self.stop = True
        else: self.stop = True
        if self.stop:
            self.i += 1
            self.j = self.i - 1
            self.stop = False
            if self.i == len(self.data): self.end = True
        return self.data

class BinaryInsertionSort(Iterator):

    def __init__(self, data: List[int]):
        super().__init__(data)
        self.i, self.j = 1, 0
        self.l, self.r = 0, 1
        self.bs = True
        self.end = False

    def getPointers(self) -> Tuple[int, int]:
        return (self.i, self.j)

    def hasNext(self) -> bool:
        return not self.end

    def next(self) -> List[int]:
        if self.bs:
            self.j = self.l + (self.r - self.l) // 2
            if self.data[self.j] < self.data[self.i]: self.l = self.j + 1
            else: self.r = self.j
            if self.l == self.r:
                self.j = self.l
                self.bs = False
                self.l = self.i - 1
        else:
            if self.j > self.l:
                self.i += 1
                self.l, self.r = 0, self.i
                self.bs = True
                if self.i == len(self.data): self.end = True
            else:
                self.data[self.l], self.data[self.l+1] = self.data[self.l+1], self.data[self.l]
                self.l -= 1
        return self.data
