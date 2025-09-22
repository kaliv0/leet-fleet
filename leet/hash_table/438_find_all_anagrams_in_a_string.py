# 438. Find All Anagrams in a String

from collections import Counter


def find_anagrams(s, p):
    result = []
    p_counter = Counter(p)
    s_counter = Counter(s[: len(p)])
    for i in range(len(s) - len(p) + 1):
        if s_counter == p_counter:
            result.append(i)
        s_counter[s[i]] -= 1
        if s_counter[s[i]] == 0:
            del s_counter[s[i]]
        if (last_ch := i + len(p)) >= len(s):
            break
        s_counter[s[last_ch]] += 1
    return result


if __name__ == "__main__":
    cases = [
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2])
    ]

    for s, p, res in cases:
        assert (actual := find_anagrams(s, p)) == res, f"{actual} != {res}, {s=}, {p=}"
