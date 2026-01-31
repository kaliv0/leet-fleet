# 22. Generate Parentheses

def generate_parenthesis(n: int) -> list[str]:
    stack = []
    result = []

    def _backtrack(left_p_count, right_p_count):
        if left_p_count < n:
            stack.append('(')
            _backtrack(left_p_count + 1, right_p_count)
            stack.pop()

        if left_p_count > right_p_count:
            stack.append(')')
            _backtrack(left_p_count, right_p_count + 1)
            stack.pop()

        if left_p_count == right_p_count == n:
            result.append("".join(stack))

    _backtrack(0, 0)
    return result


if __name__ == '__main__':
    cases = [
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (2, ["(())", "()()"]),
        (1, ["()"]),
    ]

    for n, result in cases:
        assert (actual := generate_parenthesis(n)) == result, actual
