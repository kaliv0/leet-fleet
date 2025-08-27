# 725. Split Linked List in Parts
from typing import Optional

from leet.linked_lists.utils import ListNode


def split_list_to_parts(head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
    # NB If there are N nodes in the list, and k parts, then every part has N / k elements,
    # except the first N % k parts have an extra one.
    result = []
    # find list length
    curr = head
    counter = 0
    while curr:
        counter += 1
        curr = curr.next
    # find sublist_len & lists with extra node
    sublist_len = counter // k
    longer_sublist_count = counter % k
    if longer_sublist_count:
        sublist_len += 1

    counter = 1
    curr = head
    while curr or k:
        if curr is None:
            result.append(None)
            k -= 1
            continue

        if counter == sublist_len:
            #### other version re-re-using head instead of creating new variable new_head ####
            # result.append(head)
            # head = curr.next
            # curr.next = None

            # pin next start
            new_head = curr.next
            # demarcate tail & add first sublist
            curr.next = None
            result.append(head)
            # adjust length checks
            if longer_sublist_count:
                longer_sublist_count -= 1
                if longer_sublist_count == 0:
                    sublist_len -= 1
            k -= 1
            # move pointers
            curr = new_head
            head = new_head
            counter = 1
        else:
            curr = curr.next
            counter += 1

    return result


#

def traverse_result(node_list):
    result = []
    for node in node_list:
        vals = []
        while node:
            vals.append(node.val)
            node = node.next
        result.append(vals)

    return result


if __name__ == "__main__":
    list_1 = ListNode(
        val=1, next=ListNode(
            val=2, next=ListNode(
                val=3)))
    assert (actual := traverse_result(split_list_to_parts(list_1, 5))) == [[1], [2], [3], [], []], actual

    list_2 = ListNode(
        val=1, next=ListNode(
            val=2, next=ListNode(
                val=3, next=ListNode(
                    val=4, next=ListNode(
                        val=5, next=ListNode(
                            val=6, next=ListNode(
                                val=7, next=ListNode(
                                    val=8, next=ListNode(
                                        val=9, next=ListNode(
                                            val=10))))))))))
    assert (actual := traverse_result(split_list_to_parts(list_2, 3))) == [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]], actual
