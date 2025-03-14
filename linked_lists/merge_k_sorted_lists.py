from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

    def __hash__(self):
        return hash(self.val)


def merge_two_lists(list_1: ListNode, list_2: ListNode) -> ListNode:
    head = ListNode()
    cur = head
    while list_1 and list_2:
        if list_1.val < list_2.val:
            cur.next = ListNode(val=list_1.val)
            list_1 = list_1.next
        else:
            cur.next = ListNode(val=list_2.val)
            list_2 = list_2.next

        cur = cur.next

    if list_1:
        cur.next = list_1
    else:
        cur.next = list_2

    return head.next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Time Complexity: O(k*N)
        Space Complexity: O(k*N)
        """
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            list_1 = lists.pop()
            list_2 = lists.pop()
            lists.append(merge_two_lists(list_1, list_2))

        return lists[0]
