# 49. Group Anagrams
from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result = defaultdict(list)
    for s in strs:
        result[str(sorted(s))].append(s)
    return list(result.values())
