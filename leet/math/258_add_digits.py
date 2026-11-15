# 258. Add Digits
def add_digits(num: int) -> int:
    while num >= 10:
        sum_ = 0
        while num > 0:
            num, tmp = divmod(num, 10)
            sum_ += tmp

        if sum_ < 10:
            return sum_
        num = sum_

    return num


if __name__ == "__main__":
    for num, result in (
        (38, 2),
        (0, 0),
        (1, 1),
    ):
        assert (actual := add_digits(num)) == result, actual
