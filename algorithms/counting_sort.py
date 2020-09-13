from algorithms.iterator import Iterator

class CountingSort(Iterator):

    def __init__(self, data: [int]):
        super().__init__(data)
        self.prev = data[:]
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
                for i in range(1, len(self.counts)):
                    self.counts[i] += self.counts[i-1]
                self.i = 0
        else:
            val = self.prev[self.i]
            self.data[self.counts[val] - 1] = val
            self.counts[val] -= 1
            self.i += 1
            if self.i == len(self.data): self.end = True
        return self.data
