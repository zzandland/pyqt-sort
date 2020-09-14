from algorithms.iterator import Iterator

class CountingSort(Iterator):

    def __init__(self, data: [int]):
        super().__init__(data)
        self.counting = True
        self.counts = [0] * (max(data) + 1)
        self.end = False
        self.i, self.j = 0, -1

    def getPointers(self) -> (int, int):
        return (self.i, self.j)

    def hasNext(self) -> bool:
        return not self.end

    def next(self) -> [int]:
        if self.counting:
            self.counts[self.data[self.i]] += 1
            self.i += 1
            if self.i == len(self.data):
                self.counting = False
                self.i = self.j = 0
        else:
            while not self.counts[self.j]:
                self.j += 1
            self.data[self.i] = self.j
            self.counts[self.j] -= 1
            self.i += 1
            if self.i == len(self.data): self.end = True
        return self.data
