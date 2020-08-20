from typing import List, Tuple
from algorithms.iterator import Iterator

class QuickSort(Iterator):

    def __init__(self, data: List[int]):
        super().__init__(data)
        self.st = [(0, len(data)-1)]
        self.end = False
        self.empty = True
        self.l = self.r = self.p = self.i = -1

    def getPointers(self) -> Tuple[int, int]:
        return (self.i, self.p)

    def hasNext(self) -> bool:
        return not self.end

    def next(self) -> List[int]:
        if self.empty:
            self.l, self.r = self.st.pop()
            while self.l >= self.r:
                if not self.st:
                    self.end = True
                    return self.data
                self.l, self.r = self.st.pop()
            self.p = self.l - 1
            self.i = self.l
            self.empty = False

        if self.data[self.i] < self.data[self.r]:
            self.p += 1
            self.data[self.i], self.data[self.p] = self.data[self.p], self.data[self.i]
        self.i += 1
        if self.i == self.r:
            self.p += 1
            self.data[self.r], self.data[self.p] = self.data[self.p], self.data[self.r]
            self.st.append((self.p+1, self.r))
            self.st.append((self.l, self.p-1))
            self.empty = True
        return self.data
