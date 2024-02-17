
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	var revHead *ListNode
	for head != nil {
		tmp := head.Next
		head.Next = revHead
		revHead = head
		head = tmp
	}
	return revHead
}
