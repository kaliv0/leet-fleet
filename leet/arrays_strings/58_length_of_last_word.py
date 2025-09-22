# 58. Length of Last Word


def length_of_last_word(s: str) -> int:
    # return len(s.strip().split(" ")[-1])

    if not s or s.isspace():
        return 0

    i = len(s) - 1
    length = 0
    while i >= 0:
        if not s[i].isspace():
            length += 1
        elif length > 0:
            break
        i -= 1
    return length


if __name__ == "__main__":
    assert length_of_last_word("Hello World") == 5
    assert length_of_last_word("   fly me   to   the moon  ") == 4
    assert length_of_last_word("luffy is still joyboy") == 6
