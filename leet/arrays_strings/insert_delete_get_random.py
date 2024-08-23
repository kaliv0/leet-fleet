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
    randomized_set = RandomizedSet()
    assert randomized_set.insert(1)
    assert randomized_set.remove(2) is False
    assert randomized_set.insert(2)
    assert randomized_set.get_random() in (1, 2)
    assert randomized_set.remove(1)
    assert randomized_set.insert(2) is False
    assert randomized_set.get_random() == 2

    randomized_set = RandomizedSet()
    assert randomized_set.remove(0) is False
    assert randomized_set.remove(0) is False
    assert randomized_set.insert(0)
    assert randomized_set.get_random() == 0
    assert randomized_set.remove(0)
    assert randomized_set.insert(0)

    randomized_set = RandomizedSet()
    assert randomized_set.insert(1)
    assert randomized_set.remove(1)
    assert randomized_set.insert(1)
