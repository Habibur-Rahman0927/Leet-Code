package main

import "fmt"

func canConstruct(ransomNote string, magazine string) bool {
	count := make(map[rune]int)
	for _, char := range magazine {
		count[char]++
	}

	for _, ransom := range ransomNote {
		if count[ransom] > 0 {
			count[ransom]--
		} else {
			return false
		}
	}
	return true
}

func main() {
	ransomNote := "aabb"
	magazine := "aabbc"
	result := canConstruct(ransomNote, magazine)
	fmt.Println("Can construct ransom note?", result)
}
