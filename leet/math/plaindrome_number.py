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


if __name__ == '__main__':
    assert is_palindrome(121) is True
    assert is_palindrome(-121) is False
    assert is_palindrome(1) is True
    assert is_palindrome(1221) is True
    assert is_palindrome(123) is False
