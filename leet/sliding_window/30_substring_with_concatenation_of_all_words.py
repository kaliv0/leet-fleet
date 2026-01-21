# 30. Substring with Concatenation of All Words
def find_substring(s: str, words: list[str]) -> list[int]:
    ...
    # @TODO


if __name__ == '__main__':
    for s, words, res in (
            ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
            ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
            ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
    ):
        assert (act := find_substring(s, words)) == res, f'expected: {res} != actual: {act}'
