# 2390. Removing Stars From a String


def remove_stars(s: str) -> str:
    stack = []
    for ch in s:
        if ch == "*" and stack:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


if __name__ == "__main__":
    for s, result in (
        ("leet**cod*e", "lecoe"),
        ("erase*****", ""),
    ):
        assert (actual := remove_stars(s)) == result, actual
