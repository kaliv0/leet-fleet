# 1143. Longest Common Subsequence
from collections import defaultdict


def longest_common_subsequence(text1: str, text2: str) -> int:
    dp = defaultdict(int)
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + dp[(i + 1, j + 1)]
            else:
                dp[(i, j)] = max(dp[(i, j + 1)], dp[(i + 1, j)])
    return dp[(0, 0)]


if __name__ == "__main__":
    assert (actual := longest_common_subsequence(text1="abcde", text2="ace")) == 3
    assert (actual := longest_common_subsequence(text1="abc", text2="abc")) == 3
    assert (actual := longest_common_subsequence(text1="abc", text2="def")) == 0
