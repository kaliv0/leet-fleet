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
    assert add_digits(38) == 2
    assert add_digits(0) == 0
    assert add_digits(1) == 1
