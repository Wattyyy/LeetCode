from typing import List


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.arr = []
        self.used = set()
        self.length = combinationLength
        self.string = characters
        self.idx = -1
        self.backtrack([], 0, 0)

    def backtrack(self, cur: List[int], idx: int, cnt: int) -> None:
        if cnt == self.length:
            s = "".join(cur)
            if s not in self.used:
                self.arr.append(s)
                self.used.add(s)
            return
        for i in range(idx, len(self.string)):
            cur.append(self.string[i])
            self.backtrack(cur, i + 1, cnt + 1)
            cur.pop()

    def next(self) -> str:
        self.idx += 1
        return self.arr[self.idx]

    def hasNext(self) -> bool:
        return self.idx + 1 < len(self.arr)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()


