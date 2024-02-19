package main

import "fmt"

func main() {
	nums := []int{1, 2, 2, 1, 1, 3}
	fmt.Println(uniqueOccurrences(nums))
}

func uniqueOccurrences(nums []int) bool {
	arrMap := make(map[int]int)

	for _, num := range nums {
		arrMap[num]++
	}

	uniqueCounts := make(map[int]bool)

	for _, count := range arrMap {
		if uniqueCounts[count] {
			return false
		}
		uniqueCounts[count] = true
	}
	return true
}
