# 383. Ransom Note
from collections import Counter


def can_construct(ransom_note: str, magazine: str) -> bool:
    magazine_cnt = Counter(magazine)
    note_cnt = Counter(ransom_note)
    # for k, v in note_cnt.items():
    #     if k not in magazine_cnt or magazine_cnt[k] < v:
    #         return False
    # return True

    return all(k in magazine_cnt and magazine_cnt[k] >= v for k, v in note_cnt.items())


if __name__ == "__main__":

    for note, magazine, res in (
            ("a", "b", False),
            ("aa", "ab", False),
            ("aa", "aab", True),
            ("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj", True),
    ):
        assert (actual := can_construct(note, magazine)) == res, actual
