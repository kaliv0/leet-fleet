# 380. Insert Delete GetRandom O(1)
from random import choice


class RandomizedSet:
    def __init__(self):
        self.lst = []
        self.dct = {}

    def insert(self, val: int) -> bool:
        if val not in self.dct:
            self.dct[val] = len(self.lst)
            self.lst.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dct:
            idx = self.dct[val]
            last = self.lst[-1]
            self.lst[idx] = last
            self.lst.pop()
            self.dct[last] = idx
            del self.dct[val]
            # NB: use 'idx = self.dct[val]' and 'del self.dct[val]' instead of 'self.dct.pop[val]'
            # when self.lst contains one element
            # otherwise 'self.dct[last] = idx' puts element back
            return True
        return False

    def get_random(self) -> int:
        return choice(self.lst)


if __name__ == "__main__":
    for ops in (
        [
            ("insert", 1, True),
            ("remove", 2, False),
            ("insert", 2, True),
            ("get_random_in", (1, 2)),
            ("remove", 1, True),
            ("insert", 2, False),
            ("get_random", 2),
        ],
        [
            ("remove", 0, False),
            ("remove", 0, False),
            ("insert", 0, True),
            ("get_random", 0),
            ("remove", 0, True),
            ("insert", 0, True),
        ],
        [
            ("insert", 1, True),
            ("remove", 1, True),
            ("insert", 1, True),
        ],
    ):
        rs = RandomizedSet()
        for op in ops:
            if op[0] == "insert":
                assert (actual := rs.insert(op[1])) == op[2], actual
            elif op[0] == "remove":
                assert (actual := rs.remove(op[1])) == op[2], actual
            elif op[0] == "get_random":
                assert (actual := rs.get_random()) == op[1], actual
            elif op[0] == "get_random_in":
                assert (actual := rs.get_random()) in op[1], actual
