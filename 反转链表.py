class Solution(object):
    def reverseList(self, head):
 
        p = head
        if p is None:
            return p
        s = head.next
        p.next = None
        while s is not None:
            head = s
            s = s.next
            head.next = p
            p = head
        return head
