package main

import "sort"

func main() {
	tokens := []int{100, 200, 300, 400}
	power := 200
	reuslt := BagOfTokensScore(tokens, power)
	println(reuslt)
}

func BagOfTokensScore(tokens []int, power int) int {
	res := 0
	score := 0
	sort.Ints(tokens)

	l := 0
	r := len(tokens) - 1

	for l <= r {
		if power >= tokens[l] {
			power -= tokens[l]
			l++
			score++
			if score > res {
				res = score
			}
		} else if score > 0 {
			power += tokens[r]
			r--
			score--
		} else {
			break
		}
	}
	return res
}
