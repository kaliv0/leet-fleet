# 2390. Removing Stars From a String

def remove_stars(s: str) -> str:
    stack = []
    for ch in s:
        if ch == '*' and stack:
            stack.pop()
        else:
            stack.append(ch)
    return ''.join(stack)

if __name__ == '__main__':
    assert remove_stars('leet**cod*e') == 'lecoe'
    assert remove_stars('erase*****') == ''
