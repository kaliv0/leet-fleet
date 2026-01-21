# 392. Is Subsequence
def is_subsequence(s: str, t: str) -> bool:
    if len(s) > len(t):
        return False
    if s == "":
        return True

    j = 0
    for i in range(len(t)):
        if t[i] == s[j]:
            j += 1
        if j == len(s):
            return True
    return False


def is_subsequence_diff(s: str, t: str) -> bool:
    s_ptr = 0
    t_ptr = 0
    while s_ptr < len(s) and t_ptr < len(t):
        if s[s_ptr] == t[t_ptr]:
            s_ptr += 1
        t_ptr += 1
    return s_ptr == len(s)


if __name__ == "__main__":
    assert is_subsequence("abc", "ahbgdc")
    assert is_subsequence("axc", "ahbgdc") is False
    assert is_subsequence("", "ahbgdc")
