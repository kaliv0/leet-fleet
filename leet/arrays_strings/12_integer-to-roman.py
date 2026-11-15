# 12. Integer to Roman


def int_to_roman(num: int) -> str:
    NUMS_PAIRS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = ""
    for numeral, roman in NUMS_PAIRS:
        while num >= numeral:
            result += roman
            num -= numeral
    return result


if __name__ == "__main__":
    for num, result in (
        (3, "III"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
    ):
        assert (actual := int_to_roman(num)) == result, actual
