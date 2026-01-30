# 76. Minimum Window Substring


def min_window(s: str, t: str) -> str:
    if s == t:
        return s
    elif len(s) < len(t):
        return ''

    t_counter = {}
    for c in t:
        t_counter[c] = t_counter.get(c, 0) + 1

    w_counter = {}
    min_substr = ''
    left = 0
    right = 0
    while right < len(s):
        # open window and fill counter
        if (curr_c := s[right]) in t_counter:
            w_counter[curr_c] = w_counter.get(curr_c, 0) + 1

        # if current window contains all chars from t, shrink window from the left side while it still includes t's chars
        while all(w_counter.get(k, 0) >= v for k, v in t_counter.items()):
            curr_substr = s[left: right + 1]
            # update substr on the first run (still empty) or if we've found a shorter one
            if min_substr == '' or len(curr_substr) < len(min_substr):
                min_substr = curr_substr

            # decrease counter on the left side and move pointer beyond leftmost char
            if (left_c := s[left]) in t_counter:
                w_counter[left_c] -= 1
            left += 1
        right += 1

    return min_substr


if __name__ == '__main__':
    for s, t, res in (
            ('ADOBECODEBANC', 'ABC', 'BANC'),
            ('a', 'a', 'a'),
            ('a', 'aa', ''),
            ('ab', 'A', ''),
            ('abc', 'cba', 'abc'),
    ):
        assert (act := min_window(s, t)) == res, f'{act} != {res}'
