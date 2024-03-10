package main

import "fmt"

func main() {
	nums1 := []int{1,2,2,1}
	nums2 := []int{2,2}

	result := intersection(nums1, nums2)
	fmt.Println(result)
}

func intersection(nums1 []int, num2 []int)[]int{
	nums1Set := make(map[int]bool)
	ans := []int{}

	for _, num := range nums1 {
		nums1Set[num] = true
	}

	for _, num := range nums2 {
		if nums1Set[num] {
			ans = append(ans, num)
			delete(nums1Set, num)
		}
	}
	return ans
}
