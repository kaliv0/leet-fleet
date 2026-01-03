# 68. Text Justification
def full_justify(words: list[str], max_width: int) -> list[str]:
    # build line list
    lines = []
    curr_line = []
    curr_len = 0
    i = 0
    while i < len(words):
        curr_word = words[i]
        curr_word_len = len(curr_word)
        if not curr_line:
            curr_line.append(curr_word)
            curr_len += curr_word_len
            i += 1
        elif curr_len + curr_word_len + 1 <= max_width:
            curr_line.append(curr_word)
            curr_len += curr_word_len
            curr_len += 1
            i += 1
        else:
            lines.append(curr_line[:])
            curr_line.clear()
            curr_len = 0

    if curr_len:
        lines.append(curr_line)

    # build line strings
    res = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if (len(line) == 1) or (i == len(lines) - 1):
            res.append(_justify_left(line, max_width))
        else:
            res.append(_pad_words(line, max_width))
        i += 1

    return res


def _justify_left(line, max_width):
    line_str = ''
    for word in line[:- 1]:
        line_str += word + ' '
    last_word = line[-1]
    line_str += last_word + (' ' * (max_width - (len(line_str) + len(last_word))))
    return line_str


def _pad_words(line, max_width):
    total_padding = max_width - sum(len(word) for word in line)
    pad_cnt, rem = divmod(total_padding, len(line) - 1)

    line_str = line[0]
    for i in range(1, len(line)):
        padding = ' ' * (pad_cnt + 1) if rem > 0 else ' ' * pad_cnt
        line_str += padding + line[i]
        rem -= 1

    return line_str


if __name__ == "__main__":
    for words, max_width, res in (
            (["This", "is", "an", "example", "of", "text", "justification."], 16,
             [
                 "This    is    an",
                 "example  of text",
                 "justification.  "
             ]),
            (["What", "must", "be", "acknowledgment", "shall", "be"], 16,
             [
                 # Note that the last line is "shall be    " instead of "shall     be", because the last line
                 # must be left - justified instead of fully - justified.
                 #
                 # Note that the second line is also left - justified because it contains only one word.
                 # (that is -> if the number of spaces on a line does not divide evenly between words,
                 # the empty slots on the left will be assigned more spaces than the slots on the right.)
                 "What   must   be",
                 "acknowledgment  ",
                 "shall be        "
             ]),
            (["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a",
              "computer.", "Art", "is", "everything", "else", "we", "do"], 20,
             [
                 "Science  is  what we",
                 "understand      well",
                 "enough to explain to",
                 "a  computer.  Art is",
                 "everything  else  we",
                 "do                  "
             ]),
            (["The", "important", "thing", "is", "not", "to", "stop", "questioning.", "Curiosity", "has",
              "its", "own", "reason", "for", "existing."], 17,
             [
                 "The     important",
                 "thing  is  not to",
                 "stop questioning.",
                 "Curiosity has its",
                 "own   reason  for",
                 "existing.        "
             ]),
    ):
        assert (actual := full_justify(words, max_width)) == res, actual
