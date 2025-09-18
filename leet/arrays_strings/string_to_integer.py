# 8. String to Integer (atoi)
def my_atoi(s: str) -> int:
    if len(s) == 0:
        return 0

    # skip leading white space
    i = 0
    while s[i] == " ":
        i += 1
        if i == len(s):
            return 0
        continue

    # read sign
    sign = 1
    if s[i] == "-":
        sign = -1
        i += 1
    elif s[i] == "+":
        i += 1

    res = 0
    while i < len(s) and (ch := s[i]).isdigit():
        res = res * 10 + int(ch)
        # handle overflow
        if res * sign > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res * sign < -2 ** 31:
            return -2 ** 31
        i += 1

    return res * sign


if __name__ == "__main__":
    assert my_atoi("42") == 42
    assert my_atoi(" -042") == -42
    assert my_atoi("1337c0d3") == 1337
    assert my_atoi("") == 0
    assert my_atoi(" ") == 0
    assert my_atoi("0-1") == 0
    assert my_atoi("words and 987") == 0
    assert my_atoi("-91283472332") == -2147483648
