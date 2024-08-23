# 14. Longest Common Prefix
from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    if not strs or not strs[0]:
        return ""

    for i, char in enumerate(strs[0]):
        for j in range(1, len(strs)):
            # ensure you are not outside strs[j]
            if i == len(strs[j]) or char != strs[j][i]:
                return strs[0][:i]  # cut string directly instead of building up result char by char
    # either all strings are equal or there is only one
    return strs[0]


if __name__ == "__main__":
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""
