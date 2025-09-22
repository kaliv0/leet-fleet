# 151. Reverse Words in a String
from collections import deque


def reverse_words(s: str) -> str:
    # return " ".join(reversed(s.split()))

    # remove trailing whitespaces
    left = 0
    while left < len(s) and s[left] == " ":
        left += 1

    right = len(s) - 1
    while right > left and s[right] == " ":
        right -= 1

    word_stack = deque()
    curr_word = []
    # read word by word and put on a stack
    while left <= right:
        if s[left] != " ":
            curr_word.append(s[left])
        elif s[left] == " " and curr_word:
            word_stack.appendleft("".join(curr_word))
            curr_word = []
        left += 1
    # put last word
    word_stack.appendleft("".join(curr_word))
    return " ".join(word_stack)


if __name__ == "__main__":
    assert reverse_words("the sky is blue") == "blue is sky the"
    assert reverse_words("  hello world  ") == "world hello"
    assert reverse_words("a good   example") == "example good a"
