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


if __name__ == "__main__":
    cases = [
        ("Was it a car or a cat I saw?", True),
        ("tab a cat", False),
        ("Never odd or even", True),
        (".,", True),
    ]

    for s, result in cases:
        assert (actual := is_palindrome(s)) is result, actual
