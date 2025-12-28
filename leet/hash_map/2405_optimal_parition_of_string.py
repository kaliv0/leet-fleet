# 2405. Optimal Partition of String

def partition_string(s: str) -> int:
    curr_partition = set()
    result = 1
    for ch in s:
        if ch in curr_partition:
            result += 1
            curr_partition = set()
        curr_partition.add(ch)
    return result


if __name__ == "__main__":
    assert partition_string("abacaba") == 4
    assert partition_string("ssssss") == 6
