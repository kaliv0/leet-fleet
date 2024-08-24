# 6. Zigzag Conversion
from math import ceil


def convert(s: str, rows: int) -> str:
    if rows == 1:
        return s

    # determine size and construct matrix
    section = ceil(len(s) / (2 * rows - 2.0))  # one zig-zag traversal
    rows_in_section = rows - 1
    cols = section * rows_in_section
    matrix = [[""] * cols for _ in range(rows)]

    # walk through s and write in matrix
    s_ptr = 0
    row_ptr = 0
    col_ptr = 0

    flag = True
    while flag:
        # go down
        while row_ptr < rows:
            if s_ptr == len(s):
                flag = False
                break
            matrix[row_ptr][col_ptr] = s[s_ptr]
            row_ptr += 1
            s_ptr += 1

        # re-adjust and start zigzag movement
        row_ptr -= 2
        col_ptr += 1
        while col_ptr < cols and row_ptr > 0:
            if s_ptr == len(s):
                flag = False
                break
            matrix[row_ptr][col_ptr] = s[s_ptr]
            row_ptr -= 1
            col_ptr += 1
            s_ptr += 1

    return "".join(["".join(row) for row in matrix])
    # return "".join(["".join(row) for row in matrix]).replace(" ", "")


if __name__ == "__main__":
    assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert convert("A", 1) == "A"
    assert convert("AB", 1) == "AB"
    assert convert("A", 2) == "A"
