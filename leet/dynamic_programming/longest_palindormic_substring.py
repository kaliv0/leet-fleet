def longest_palindrome(s):
    # empty in single-char string are themselves palindromes
    if len(s) in {0, 1}:
        return s

    # if no other palindromes are found first character is considered as such (?!)
    longest_palin = s[0]
    for i in range(1, len(s)):
        # check odd-numbered lengths (aba)
        curr_palin = expand_palindrome(s, left=i - 1, right=i + 1)
        if len(curr_palin) > len(longest_palin):
            longest_palin = curr_palin
        if s[i] == s[i - 1]:
            # check even-numbered (abba)
            curr_palin = expand_palindrome(s, left=i - 1, right=i)
            if len(curr_palin) > len(longest_palin):
                longest_palin = curr_palin

    return longest_palin


def expand_palindrome(s, left, right):
    palindrome = ""
    while left >= 0 and right < len(s):
        if s[left] != s[right]:
            break
        palindrome = s[left: right + 1]
        left = left - 1
        right = right + 1
    return palindrome


if __name__ == "__main__":
    cases = [
        ("a", "a"),
        ("", ""),
        ("ac", "a"),
        ("aa", "aa"),
        ("bcabad", "aba"),
        ("cbbd", "bb"),
    ]

    for s, res in cases:
        assert (actual := longest_palindrome(s)) == res, \
            f"{actual} != {res}, {s=}"
