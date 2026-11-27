class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Advance `fast` by `n + 1` steps so there are `n` nodes between `slow` and `fast`
        for _ in range(n + 1):
            if fast:
                fast = fast.next

        # Move both pointers until `fast` reaches None
        while fast:
            slow = slow.next
            fast = fast.next

        # `slow.next` is the target node to remove
        if slow.next:
            slow.next = slow.next.next

        return dummy.next