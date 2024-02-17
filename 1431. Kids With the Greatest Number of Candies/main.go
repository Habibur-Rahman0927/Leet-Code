package main

import (
	"fmt"
)

func main() {
	fmt.Println("hello")
	candies := []int{2, 3, 5, 1, 3}
	extraCandies := 3
	fmt.Println(kidsWithCandies(candies, extraCandies))
}

func kidsWithCandies(candies []int, extraCandies int) []bool {
	length := len(candies)
	result := make([]bool, length)
	max_number := max(candies...)
	for i, candie := range candies {
		if candie+extraCandies >= max_number {
			result[i] = true
		}
	}
	return result
}

func max(nums ...int) int {
	if len(nums) == 0 {
		return -1 // return -1 for empty input or error handling
	}

	max := nums[0] // Initialize max to the first element

	for _, num := range nums {
		if num > max {
			max = num
		}
	}

	return max
}
