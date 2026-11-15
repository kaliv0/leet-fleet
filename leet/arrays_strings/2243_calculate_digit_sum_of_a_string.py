# 2243. Calculate Digit Sum of a String
def digit_sum(s: str, k: int) -> str:
    while len(s) > k:
        digits = []
        for i in range(0, len(s), k):
            digits.append(str(sum(int(d) for d in s[i : i + k])))
        s = "".join(digits)

    return s


if __name__ == "__main__":
    for s, k, result in (
        ("11111222223", 3, "135"),
        ("00000000", 3, "000"),
    ):
        assert (actual := digit_sum(s, k)) == result, actual
