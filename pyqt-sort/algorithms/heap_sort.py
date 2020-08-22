from algorithms.iterator import Iterator
from typing import List, Tuple

class HeapSort(Iterator):

    def __init__(self, data: List[int]):
        super().__init__(data)

    def getPointers(self) -> Tuple[int, int]:
        pass

    def hasNext(self) -> bool:
        pass

    def next(self) -> List[int]:
        pass
