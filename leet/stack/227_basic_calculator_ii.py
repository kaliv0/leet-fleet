# 227. Basic Calculator II
def calculate(s: str) -> int:
    stack = []
    num = 0
    sign = '+'

    for i in range(len(s)):
        ch = s[i]
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch in '+-*/':
            _add_to_stack(stack, num, sign)
            num = 0
            sign = ch

    _add_to_stack(stack, num, sign)
    return sum(stack)


def _add_to_stack(stack: list[int], num: int, sign: str):
    match sign:
        case '+':
            stack.append(num)
        case '-':
            stack.append(-num)
        case '*':
            stack.append(stack.pop() * num)
        case '/':
            prev = stack.pop()
            sign = -1 if prev < 0 else 1
            stack.append(sign * (abs(prev) // num))


if __name__ == "__main__":
    for s, res in (
            ("14-3/2", 13),
            ("3+2*2", 7),
            (" 3/2 ", 1),
            (" 3+5 / 2 ", 5)
    ):
        assert (actual := calculate(s)) == res, actual
