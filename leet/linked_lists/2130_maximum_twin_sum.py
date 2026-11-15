# 2130. Maximum Twin Sum of a Linked List

from leet.linked_lists.utils import ListNode, build_list


# NB: number of nodes is always even, sum is always positive
def pair_sum(head):
    # find middle node
    middle_node = find_middle_node(head)
    # reverse second half ot list
    new_head = reverse_list(middle_node.next)
    middle_node.next = new_head
    # traverse with 2 pointers form both ends
    #   -> find twin sum at each step and store in total if biggest so far
    max_sum = 0
    left = head
    right = new_head
    while right:
        max_sum = max(left.val + right.val, max_sum)

        left = left.next
        right = right.next

    return max_sum


def find_middle_node(head):
    fast = head
    slow = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def reverse_list(head):
    prev = None
    curr = head
    temp = head.next
    while temp:
        curr.next = prev
        prev = curr
        curr = temp
        temp = curr.next

    curr.next = prev
    return curr


if __name__ == "__main__":
    for inp, result in (
        ([5, 4, 2, 1], 6),
        ([4, 2, 2, 3], 7),
        ([1, 100000], 100001),
    ):
        assert (actual := pair_sum(build_list(inp))) == result, actual
