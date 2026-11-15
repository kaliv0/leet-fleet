# 2. Merge Two Numbers

from leet.linked_lists.utils import ListNode, build_list, traverse_list


def add_two_numbers(
    first_list: ListNode | None, second_list: ListNode | None
) -> ListNode | None:
    # when creating dynamically new linked_list -> start with a dummy_node
    dummy = ListNode()
    curr_node = dummy
    carry = 0
    # even if both lists are done there could still be carry val for the next node in the result
    while first_list or second_list or carry:
        # if first_list & second_list are different length -> adjust to return val=0 for shorter list
        curr_sum = (
            (first_list.val if first_list else 0)
            + (second_list.val if second_list else 0)
            + carry
        )
        # next two lines are actually used only if curr_sum >= 10
        # but could be used in all cases carry = curr_sum // 10 yields 0 fir curr_sum < 10
        if curr_sum >= 10:
            carry = curr_sum // 10
            curr_sum = curr_sum % 10
        else:
            carry = 0
        curr_node.next = ListNode(val=curr_sum)
        # move pointers ahead
        curr_node = curr_node.next
        first_list = first_list and first_list.next
        second_list = second_list and second_list.next

    return dummy.next


if __name__ == "__main__":
    for a, b, result in (
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ):
        assert (
            actual := traverse_list(add_two_numbers(build_list(a), build_list(b)))
        ) == result, actual
