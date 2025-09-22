# ???

def longest_subsequence(s):
    if not s:
        return 0

    if len(s) == 1:
        return 1

    max_len = 0
    start = 0
    end = 1
    curr_char = s[0]
    curr_char_idx = 0
    visited = {curr_char}

    while start < len(s) and end < len(s):
        curr_char = s[end]
        visited.add(curr_char)
        if len(visited) == 3:
            visited.clear()
            max_len = max(max_len, end - start)
            start = curr_char_idx
        end += 1
        if curr_char != s[end - 1]:
            curr_char_idx = end

    return max(max_len, end - start)


if __name__ == "__main__":
    cases = [
        ("", 0),
        ("a", 1),
        ("aaab", 4),
        # ("cdaba", 3),
        # ("eceba", 3),
        ("ccaaabbb", 6),
        ("aababbaacacaacacccaabad", 14),  # aacacaacacccaa
    ]

    for s, length in cases:
        assert (actual := longest_subsequence(s)) == length, \
            f"{actual} != {length}, {s=}"
