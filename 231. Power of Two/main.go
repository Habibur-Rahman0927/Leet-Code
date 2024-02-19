package main

import "fmt"

func main() {
	fmt.Println(isPowerOfTwo(512))
}

func isPowerOfTwo(n int) bool {
	if n <= 0 {
		return false
	}
	if n == 1 {
		return true
	}
	for n%2 == 0 {
		n = n / 2
	}
	return n == 1
}
