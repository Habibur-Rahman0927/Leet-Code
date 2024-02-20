# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # l1, l2 = headA, headB
        # while l1 != l2:
        #     l1 = l1.next if l1 else headB
        #     l2 = l2.next if l2 else headA
        # return l1

        lenA, lenB = 0, 0
        l1, l2 = headA, headB
        while l1 or l2:
            if l1:
                l1 = l1.next
                lenA += 1
            if l2:
                l2 = l2.next
                lenB += 1
        
        l1, l2 = headA, headB
        
        while lenA > lenB:
            l1 = l1.next
            lenA -= 1
        while lenB > lenA:
            l2 = l2.next
            lenB -= 1
        
        while l1 and l2:
            if l1 == l2:
                return l1
            else:
                l1 = l1.next
                l2 = l2.next
            
        return None