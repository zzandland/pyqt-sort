from algorithms.iterator import Iterator
from typing import List, Tuple

class MergeSort(Iterator):

    def __init__(self, data: List[int]):
        super().__init__(data)
        self.st = [(0, len(data)-1)]
        self.seen = set()
        self.merge = False
        self.tmp = []
        self.l1 = self.l2 = self.r1 = self.r2 = -1

    def getPointers(self) -> Tuple[int, int]:
        return (self.l1, self.l2)

    def hasNext(self) -> bool:
        return bool(self.st)

    def next(self) -> List[int]:
        if self.merge:
            if self.l2 > self.r2:
                self.tmp.append(self.data[self.l1])
                self.l1 += 1
            elif self.l1 > self.r1:
                self.tmp.append(self.data[self.l2])
                self.l2 += 1
            else:
                if self.data[self.l1] < self.data[self.l2]:
                    self.tmp.append(self.data[self.l1])
                    self.l1 += 1
                else:
                    self.tmp.append(self.data[self.l2])
                    self.l2 += 1
            if self.l1 > self.r1 and self.l2 > self.r2:
                l, r = self.st[-1]
                self.data[l:r+1] = self.tmp
                self.merge = False
                self.tmp = []
        else:
            while self.st and not self.merge:
                l, r = self.st.pop()
                if not self.st and (l, r) in self.seen:
                    self.end = True
                elif not self.st or (l, r) not in self.seen:
                    self.seen.add((l, r))
                    if l < r:
                        m = l + (r-l) // 2
                        self.st += [(m+1, r), (l, m)]
                    else:
                        self.st.append((l, r))
                elif (l, r) in self.seen:
                    if self.st[-1] in self.seen: self.prepareMerge(l, r)
                    else:
                        tmp = self.st.pop()
                        self.st.append((l, r))
                        self.st.append(tmp)
        return self.data

    def prepareMerge(self, l2: int, r2: int) -> None:
        l1, r1 = self.st.pop()
        self.st.append((l1, r2))
        self.l1, self.l2 = l1, l2
        self.r1, self.r2 = r1, r2
        self.merge = True
