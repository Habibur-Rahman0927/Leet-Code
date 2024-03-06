# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return False
        fp = head.next
        sp = head
        while fp and sp:
            if fp==sp:
                return True
            sp = sp.next
            if fp.next:
                fp = fp.next.next
            else:
                return False
        
        return False
        
        