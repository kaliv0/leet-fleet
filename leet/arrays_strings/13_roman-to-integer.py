# 13. Roman to Integer


def roman_to_int(s: str) -> int:
    NUMS_MAP = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    result = 0
    prev = 0
    for i in s[::-1]:
        curr = NUMS_MAP[i]
        if prev > curr:
            result -= curr
        else:
            result += curr
        prev = curr
    return result


if __name__ == "__main__":
    for s, result in (
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ):
        assert (actual := roman_to_int(s)) == result, actual
