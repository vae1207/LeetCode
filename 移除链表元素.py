class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        while head is not None and head.val == val:
            head = head.next
        p = head
        while p is not None and p.next is not None:
            if p.next.val != val:
                p = p.next
            else:
                p.next = p.next.next
        return head
                
