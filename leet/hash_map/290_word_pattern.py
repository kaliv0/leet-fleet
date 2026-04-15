def word_pattern(pattern: str, s: str) -> bool:
    words = s.split(' ')
    if len(words) != len(pattern):
        return False

    word_2_char = {}
    char_2_word = {}
    for char, word in zip(pattern, words):
        if char not in char_2_word:
            if word in word_2_char:
                return False
            char_2_word[char] = word
            word_2_char[word] = char
        if char_2_word[char] != word:
            return False

    return True


if __name__ == '__main__':
    for i, (p, s, res) in enumerate((
            ("abba", "dog cat cat dog", True),
            ("abba", "dog dog dog dog", False),
            ("abba", "dog cat cat fish", False),
            ("aaaa", "dog cat cat dog", False)
    )):
        assert (act := word_pattern(p, s)) == res, f"{act} != {res}, {i=}"
