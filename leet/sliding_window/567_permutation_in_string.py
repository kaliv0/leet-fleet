# 567. Permutation in String

LETTERS = 26


def check_inclusion(s1: str, s2: str) -> bool:
    # check string lengths
    if len(s1) > len(s2):
        return False

    counter1 = [0] * LETTERS
    counter2 = [0] * LETTERS
    # basically create counter for s1 and start creating counter for s2
    for i in range(len(s1)):
        counter1[get_index(s1[i])] += 1
        counter2[get_index(s2[i])] += 1

    # calculate initial matches
    matches = 0
    for i in range(LETTERS):
        if counter1[i] == counter2[i]:
            matches += 1

    left = 0
    # start sliding window to read rest of s2
    for right in range(len(s1), len(s2)):
        if matches == LETTERS:
            return True

        # read right char
        idx = get_index(s2[right])
        counter2[idx] += 1
        # adjust matches
        if counter2[idx] == counter1[idx]:
            matches += 1
        elif counter2[idx] - 1 == counter1[idx]:
            matches -= 1

        # read left char
        idx = get_index(s2[left])
        counter2[idx] -= 1
        # adjust matches
        if counter2[idx] == counter1[idx]:
            matches += 1
        elif counter2[idx] + 1 == counter1[idx]:
            matches -= 1

        # we move entire window with each iteration keeping constant window size
        left += 1

    return matches == LETTERS


def get_index(ch):
    return ord(ch) - ord("a")


if __name__ == "__main__":
    assert check_inclusion(s1="ab", s2="eidbaooo") == True
    assert check_inclusion(s1="ab", s2="eidboaoo") == False
