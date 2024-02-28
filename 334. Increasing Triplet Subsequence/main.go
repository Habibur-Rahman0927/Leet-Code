package main

import (
	"fmt"
	"math"
)

func main() {
	nums := []int{1, 2, 3, 4, 5}
	fmt.Println(increasingTriplet(nums))
}

func increasingTriplet(nums []int) bool {
	if len(nums) < 3 {
		return false
	}

	min1 := math.MaxInt64
	min2 := math.MaxInt64

	for _, num := range nums {
		if num <= min1 {
			min1 = num
		} else if num <= min2 {
			min2 = num
		} else {
			return true
		}
	}
	return false
}
