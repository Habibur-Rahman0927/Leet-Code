package main

import "fmt"

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	// fmt.Println(twoSum(nums, target))
	fmt.Println(twoSumUsingMap(nums, target))
}

func twoSum(nums []int, target int) []int {
	result := make([]int, 2)

	for num1 := 0; num1 < len(nums); num1++ {
		for num2 := num1 + 1; num2 < len(nums); num2++ {
			if nums[num1]+nums[num2] == target {
				result[0] = num1
				result[1] = num2
				return result
			}
		}
	}
	return result
}

func twoSumUsingMap(nums []int, target int) []int {
	numToIndex := make(map[int]int)

	for i, num := range nums {
		complement := target - num
		if idx, found := numToIndex[complement]; found {
			return []int{idx, i}
		}
		numToIndex[num] = i
	}
	return []int{}
}
