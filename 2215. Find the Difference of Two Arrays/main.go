package main

import "fmt"

func main() {
	nums1 := []int{1, 2, 3}
	nums2 := []int{2, 4, 6}
	fmt.Println(findMissing(nums1, nums2))
}

func findMissing(nums1 []int, nums2 []int) [][]int {
	set1 := make(map[int]bool)
	set2 := make(map[int]bool)

	for _, num := range nums1 {
		set1[num] = true
	}

	for _, num := range nums2 {
		set2[num] = true
	}

	missing1 := make([]int, 0)
	missing2 := make([]int, 0)

	for num := range set1 {
		if !set2[num] {
			missing1 = append(missing1, num)
		}
	}

	for num := range set2 {
		if !set1[num] {
			missing2 = append(missing2, num)
		}
	}

	return [][]int{missing1, missing2}
}
