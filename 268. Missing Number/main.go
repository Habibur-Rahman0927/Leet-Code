package main

import (
	"fmt"
)

func main() {
	nums := []int{3, 0, 1}
	fmt.Println(missingNumber(nums))
}

func missingNumber(nums []int) int {
	// sort.Ints(nums)
	// for i := 0; i < len(nums); i++ {
	// 	if i != nums[i] {
	// 		return i
	// 	}
	// }
	// return len(nums)

	n := len(nums) + 1
	return ((len(nums) * n) / 2) - Sum(nums)
}

func Sum(numbers []int) int {
	sum := 0
	for _, num := range numbers {
		sum += num
	}
	return sum
}
