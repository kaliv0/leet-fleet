# 125. Valid Palindrome
def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        while s[left].isalnum() is False and left < right:
            left += 1
        while s[right].isalnum() is False and right > left:
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True


if __name__ == '__main__':
    assert is_palindrome("Was it a car or a cat I saw?") is True
    assert is_palindrome("tab a cat") is False
    assert is_palindrome("Never odd or even") is True
    assert is_palindrome(".,") is True
