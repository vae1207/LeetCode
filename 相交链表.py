class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        b = headB
        a_num = 0
        b_num = 0
        while a:
            a = a.next
            a_num += 1
        while b:
            b = b.next
            b_num += 1
        
        if a_num > b_num:
            gap = a_num - b_num
            while gap:
                headA = headA.next
                gap -= 1
            while headA and headB:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
            return
        else:
            gap = b_num - a_num
            while gap:
                headB = headB.next
                gap -= 1
            while headA and headB:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
            return
