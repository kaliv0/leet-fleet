# 205. Isomorphic Strings
def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}
    for char_s, char_t in zip(s, t):
        if (char_s in s_to_t and s_to_t[char_s] != char_t) or (
            char_t in t_to_s and t_to_s[char_t] != char_s
        ):
            return False
        s_to_t[char_s] = char_t
        t_to_s[char_t] = char_s

    return True


if __name__ == "__main__":
    for s, t, flag in (
            ("egg", "add", True),
            ("foo", "bar", False),
            ("paper", "title", True),
    ):
        assert (act := is_isomorphic(s, t)) == flag, f"{act} != {flag}"
