# 9. Palindrome Number
def is_palindrome(x):
    if x < 0:
        return False

    rev = 0
    tmp = x
    while tmp:
        rev = (rev * 10) + tmp % 10
        tmp = tmp // 10

    return x == rev


if __name__ == "__main__":
    cases = [
        (121, True),
        (-121, False),
        (1, True),
        (1221, True),
        (123, False),
    ]

    for x, result in cases:
        assert (actual := is_palindrome(x)) == result, actual
