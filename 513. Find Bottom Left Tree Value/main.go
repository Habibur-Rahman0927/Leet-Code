package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findLastLevelLeftValue(root *TreeNode) int {
	if root == nil {
		return 0
	}
	queue := []*TreeNode{root}
	var lastLevelLeftValue int
	for len(queue) > 0 {
		size := len(queue)
		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]
			if i == 0 {
				lastLevelLeftValue = node.Val
			}
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
	}
	return lastLevelLeftValue
}

func main() {
	root := &TreeNode{Val: 1}
	root.Left = &TreeNode{Val: 2}
	root.Right = &TreeNode{Val: 3}
	root.Left.Left = &TreeNode{Val: 4}
	root.Left.Right = &TreeNode{Val: 5}
	root.Right.Left = &TreeNode{Val: 6}
	root.Right.Right = &TreeNode{Val: 7}

	lastLevelLeftValue := findLastLevelLeftValue(root)
	fmt.Println("Value of the leftmost node in the last level: ", lastLevelLeftValue)
}
