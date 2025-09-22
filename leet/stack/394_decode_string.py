# 394. Decode String

def decode_string(s: str) -> str:
    stack = []
    for c in s:
        if c != ']':
            stack.append(c)
        else:
            # pop back nested substring
            substr = ''
            while stack[-1] != '[':
                substr = stack.pop() + substr
            stack.pop()  # pop the actual '['

            # build k to multiply nested substr
            k = ''
            while stack and stack[-1].isdigit():
                k = stack.pop() + k

            stack.append(int(k) * substr)
    return ''.join(stack)


if __name__ == "__main__":
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"