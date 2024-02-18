package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(reverseWords("the sky is blue"))
}
func reverseWords(s string) string {
	stringToArray := strings.Split(s, " ")
	result := make([]string, 0, len(stringToArray))

	for i := len(stringToArray) - 1; i >= 0; i-- {
		if stringToArray[i] != "" {
			result = append(result, stringToArray[i])
		}
	}
	return strings.Join(result, " ")
}
