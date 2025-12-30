# 17. Letter Combinations of a Phone Number

digits_2_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}


def letter_combinations(digits: str) -> list[str]:
    res = []
    dfs(digits, '', 0, res)
    return res


def dfs(nums, candidate, idx, res):
    if idx == len(nums):
        res.append(candidate)
        return

    curr_letters = digits_2_letters[nums[idx]]
    for curr_char in curr_letters:
        # we add current char as new_candidate and move idx to next digit
        # -> we want to combine curr_char with letters from next digit
        new_candidate = candidate + curr_char
        next_idx = idx + 1
        dfs(nums, new_candidate, next_idx, res)


if __name__ == "__main__":
    for digits, res in (
            ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
            ("2", ["a", "b", "c"]),
    ):
        assert (actual := letter_combinations(digits)) == res, actual
