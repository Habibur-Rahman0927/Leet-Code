# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyHead = ListNode(None)
        dummyHead.next = head
        node = dummyHead

        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return dummyHead.next