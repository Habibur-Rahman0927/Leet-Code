package main

import "fmt"

func main() {
	fmt.Println(pivotInteger(8))
}

func pivotInteger(n int) int {
	numbers := make([]int, n)
	for i := 1; i <= n; i++ {
		numbers[i-1] = i
	}

	for pivot := 0; pivot < n; pivot++ {
		after := sum(numbers[:pivot+1])
		before := sum(numbers[pivot:])
		if after == before {
			return pivot + 1
		}
	}
	return -1
}

func sum(nums []int) int {
	sum := 0
	for _, num := range nums {
		sum += num
	}
	return sum
}
