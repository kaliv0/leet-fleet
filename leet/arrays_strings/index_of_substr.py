# 28. Find the Index of the First Occurrence in a String


def str_str(haystack: str, needle: str) -> int:
    haystack_len = len(haystack)
    needle_len = len(needle)
    for i in range(haystack_len - needle_len + 1):
        for j in range(needle_len):
            if needle[j] != haystack[i + j]:
                break
            if j == needle_len - 1:
                return i
    return -1


if __name__ == "__main__":
    assert str_str("sadbutsad", "sad") == 0
    assert str_str("leetcode", "leeto") == -1
