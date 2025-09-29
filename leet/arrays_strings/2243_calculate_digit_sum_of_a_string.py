# 2243. Calculate Digit Sum of a String
def digit_sum(s: str, k: int) -> str:
    while len(s) > k:
        digits = []
        for i in range(0, len(s), k):
            digits.append(str(sum(int(d) for d in s[i:i + k])))
        s = "".join(digits)

    return s


if __name__ == "__main__":
    assert digit_sum(s="11111222223", k=3) == "135"
    assert digit_sum(s="00000000", k=3) == "000"
