def find_and_replace_pattern(words: list[str], pattern: str) -> list[str]:
    def _validate(word: str) -> bool:
        if len(word) != len(pattern):
            return False

        w_2_p = {}
        p_2_w = {}
        for word_ch, ptrn_ch in zip(word, pattern):
            if word_ch not in w_2_p:
                if ptrn_ch in p_2_w:
                    return False
                w_2_p[word_ch] = ptrn_ch
                p_2_w[ptrn_ch] = word_ch
            if w_2_p[word_ch] != ptrn_ch:
                return False

        return True

    res = []
    for word in words:
        if _validate(word):
            res.append(word)

    return res


if __name__ == '__main__':
    for idx, (words, pattern, res) in enumerate((
            (["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb", ["mee", "aqq"]),
            (["a", "b", "c"], "a", ["a", "b", "c"]),
    )):
        assert (act := find_and_replace_pattern(words, pattern)) == res, f"{act} != {res}, {idx=}"
