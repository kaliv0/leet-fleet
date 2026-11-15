# 150. Evaluate Reverse Polish Notation

import operator

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def evalRPN(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if not token.strip("-").isnumeric():
            y, x = stack.pop(), stack.pop()
            token = OPERATORS[token](x, y)
        stack.append(int(token))
    return stack.pop()


if __name__ == "__main__":
    for tokens, result in (
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ):
        assert (actual := evalRPN(tokens)) == result, actual

# NB: The division between two integers always truncates toward zero
# => use int(x / y) instead of (x // y) if y is negative
# => (6 // -132) = -1; int(6 / -132)) = 0
