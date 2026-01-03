# 139. Word break
def word_break(s: str, word_dict: list[str]) -> bool:
    memo = {}

    def _dp(s):
        if s in word_dict:
            return True

        if s in memo:
            return memo[s]

        for i in range(1, len(s)):
            if _dp(s[:i]) and _dp(s[i:]):
                memo[s] = True
                return True
        memo[s] = False
        return False

    return _dp(s)


if __name__ == "__main__":
    for s, word_dict, res in (
            ("leetcode", ["leet", "code"], True),
            ("applepenapple", ["apple", "pen"], True),
            ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ):
        assert (actual := word_break(s, word_dict)) == res, actual
