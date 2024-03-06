package main

// Definition for singly-linked list.
type ListNode struct {
    Val  int
    Next *ListNode
}

func main()  {
	node1 := &ListNode{Val: 1}
    node2 := &ListNode{Val: 2}
    node3 := &ListNode{Val: 3}
    node4 := &ListNode{Val: 4}

	result := hasCycle(node1)
    fmt.Println(result)
}

func hasCycle(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return false
	}

	fp := head.Next
	sp := head
	for fp != nil && sp != nil {
		if fp == sp {
			return true
		}
		sp = sp.Next
		if fp.Next != nil {
			fp = fp.Next.Next
		}else{
			return false
		}
	}
	return false
}

