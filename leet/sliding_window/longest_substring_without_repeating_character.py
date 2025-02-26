# 3. Longest Substring Without Repeating Characters


def length_of_longest_substring(s: str) -> int:
    left = 0
    char_set = set()
    result = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        result = max(result, right - left + 1)
    return result


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
