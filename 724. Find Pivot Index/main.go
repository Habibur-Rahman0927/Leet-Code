package main

import "fmt"

func main() {
	array := []int{1, 7, 3, 6, 5, 6}
	fmt.Println(pivotIndex(array))
}

func pivotIndex(nums []int) int {
	totalSum := 0
	for _, num := range nums {
		totalSum += num
	}

	leftSum := 0
	for i, num := range nums {
		if leftSum == totalSum-leftSum-num {
			return i
		}
		leftSum += num
	}

	return -1
}
