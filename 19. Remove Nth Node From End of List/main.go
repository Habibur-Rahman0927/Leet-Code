package main

// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

func main() {
	n := 2

	// removeNthFromEnd(&ListNode, n)
	testNode := []int{1, 2, 3, 4, 5}
	removeNthFromEnd(testNode, n)
}
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	if head == nil || (head.Next == nil && n == 1) {
		return nil
	}
	count := 0
	temp := head
	for temp != nil && temp.Next != nil {
		temp = temp.Next
		count++
	}
	nth_node := count - n
	if nth_node < 0 {
		head = head.Next
		return head
	}
	i := 0
	slow := head
	for i < nth_node {
		slow = slow.Next
		i++
	}
	slow.Next = slow.Next.Next

	return head
}
