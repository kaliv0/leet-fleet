# 79. Word Search
def exist(board: list[list[str]], word: str) -> bool:
    def _backtrack(i: int, j: int, k: int) -> bool:
        # we've reach the end of the word
        if k == len(word):
            return True
        # we are outside the board boundaries
        if (i < 0 or i >= len(board)) or (j < 0 or j >= len(board[0])):
            return False
        # current char is incorrect (NB: because of previous check our curr position is guaranteed to be valid)
        if board[i][j] != word[k]:
            return False

        # backtrack
        tmp = board[i][j]
        board[i][j] = ''  # mark as read

        # search adjacent squares of next char (i.e. next word idx)
        next_word_idx = k + 1
        if _backtrack(i + 1, j, next_word_idx) \
            or _backtrack(i, j + 1, next_word_idx) \
            or _backtrack(i - 1, j, next_word_idx) \
            or _backtrack(i, j - 1, next_word_idx):
            return True

        board[i][j] = tmp  # bring init val
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if _backtrack(i, j, 0):
                return True
    return False


if __name__ == "__main__":
    for board, word, res in (
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True),
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True),
            ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False),
    ):
        assert (actual := exist(board, word)) == res, actual
