package main

import {
	"fmt"
	"sort"
}

func main() {
	order := "cba"
	s := "abcd"
	fmt.Println(customSortString(order, s))
}

func customSortString(order string, s string) string {
	lk := make(map[rune]int)
	for i, c := range order {
		lk[c] = i
	}

	runes := []rune(s)
	sort.SliceStable(runes, func(i, j int)bool{
		return lk[runes[i]] < lk[runes[j]]
	})

	return string(runes)
}