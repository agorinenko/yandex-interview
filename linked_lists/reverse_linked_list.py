from typing import Optional

from linked_lists.merge_k_sorted_lists import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """""
        # 1->2->3->4
        # prev<-1<-2->3->4
        prev= None
        cur = head
        while cur:
            # Создаем временный указатель на next, чтобы затем сдвинуть cur
            next_ptr = cur.next
            # Обновляем указатель cur.next на prev
            cur.next = prev
            # делаем prev cur'ом
            prev = cur
            # двигаем cur
            cur = next_ptr

        return prev
