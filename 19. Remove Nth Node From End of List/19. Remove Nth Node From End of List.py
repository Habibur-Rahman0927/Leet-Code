# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # dummy = ListNode(0, head)
        # left = dummy
        # right = head

        # while n > 0 and right:
        #     right = right.next
        #     n -= 1
        # while right:
        #     left = left.next
        #     right = right.next
        # left.next = left.next.next
        # return dummy.next

        if (head == None or head.next == None) and n == 1: 
            return None
        count = 0
        temp = head
        while temp and temp.next:
            temp = temp.next
            count += 1
        nth_position = count - n
        
        if nth_position < 0:
            head = head.next
            return head

        slow = head
        i = 0
        while i < nth_position:
            slow = slow.next
            i += 1
        slow.next = slow.next.next
        return head