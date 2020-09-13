from algorithms.iterator import Iterator
from typing import List, Tuple

class HeapSort(Iterator):

    def __init__(self, data: List[int]):
        super().__init__(data)
        self.i = self.j = len(self.data) // 2 - 1
        self.isHeap = False
        self.end = False

    def getPointers(self) -> Tuple[int, int]:
        return (self.i, self.j)

    def hasNext(self) -> bool:
        return not self.end

    def next(self) -> List[int]:
        if self.isHeap:
            self.heapify(self.i)
            if self.i == -1: self.end = True
        else:
            self.heapify(len(self.data)-1)
            if self.i == -1:
                self.i = len(self.data) - 1
                self.j = 0
                self.isHeap = True
        return self.data

    def heapify(self, N: int) -> None:
        largest = self.j
        l, r = largest*2 + 1, largest*2 + 2
        if l <= N and self.data[largest] < self.data[l]: largest = l
        if r <= N and self.data[largest] < self.data[r]: largest = r
        if largest != self.j:
            self.data[largest], self.data[self.j] = self.data[self.j], self.data[largest]
            self.j = largest
        else:
            if self.isHeap: self.data[0], self.data[self.i] = self.data[self.i], self.data[0]
            self.i -= 1
            self.j = 0 if self.isHeap else self.i
