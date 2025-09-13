# 242. Valid Anagram

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counter = {}  # we could always use default dict or Counter
    for i in range(len(s)):
        if s[i] not in counter:
            counter[s[i]] = 0
        counter[s[i]] += 1
        if t[i] not in counter:
            counter[t[i]] = 0
        counter[t[i]] -= 1

    return all(n == 0 for n in counter.values())


if __name__ == "__main__":
    assert is_anagram(s="anagram", t="nagaram") is True
    assert is_anagram(s="rat", t="car") is False
