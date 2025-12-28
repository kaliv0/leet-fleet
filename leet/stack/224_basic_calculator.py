# 224. Basic Calculator
def calculate(s: str) -> int:
    return _calculate(s, 0)[0]


def _calculate(s: str, idx: int) -> tuple[int, int]:
    stack = []
    num = 0
    sign = '+'
    while idx < len(s):
        match ch := s[idx]:
            case '+':
                _append_to_stack(num, sign, stack)
                num = 0
                sign = '+'
            case '-':
                _append_to_stack(num, sign, stack)
                num = 0
                sign = '-'
            case '(':
                num, adv_idx = _calculate(s, idx + 1)
                idx = adv_idx
            case ')':
                _append_to_stack(num, sign, stack)
                return sum(stack), idx
            case _ as d if d.isdigit():
                num = num * 10 + int(ch)

        idx += 1

    _append_to_stack(num, sign, stack)
    return sum(stack), idx


def _append_to_stack(num: int, sign: str, stack: list[int]) -> None:
    match sign:
        case '+':
            stack.append(num)
        case '-':
            stack.append(-num)


if __name__ == "__main__":
    for s, res in (
            ("1 + 1", 2),
            (" (2-1) + 2 ", 3),
            (" 24-1 + 2 ", 25),
            ("(1+(4+5+2)-3)+(6+8)", 23),
    ):
        assert (actual := calculate(s)) == res, actual
