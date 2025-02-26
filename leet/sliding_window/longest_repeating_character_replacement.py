# 424. Longest Repeating Character Replacement
from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
    left = 0
    counter = defaultdict(int)
    result = 0
    max_frequency = 0

    for right in range(len(s)):
        curr_char = s[right]
        counter[curr_char] += 1
        max_frequency = max(max_frequency, counter[curr_char])

        while (right - left + 1) - max_frequency > k:
            counter[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result


if __name__ == "__main__":
    assert character_replacement(s="ABAB", k=2) == 4
    assert character_replacement(s="AABABBA", k=1) == 4
