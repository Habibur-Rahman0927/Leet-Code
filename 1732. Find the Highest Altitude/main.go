package main

import "math"

func main() {
	gain := []int{-5, 1, 5, 0, -7}
	largestAltitude(gain)
}

func largestAltitude(gain []int) int {
	result := 0
	sum := 0
	for _, g := range gain {
		sum = sum + g
		result = int(math.Max(float64(sum), float64(result)))
	}
	return result
}
