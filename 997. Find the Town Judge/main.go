package main

func main() {
	n := 3
	trust := [][]int{{1, 3}, {2, 3}, {3, 1}}
	findJudge(n, trust)
}

func findJudge(n int, trust [][]int) int {
	count := make([]int, n+1)

	for _, t := range trust {
		a, b := t[0], t[1]
		count[a]--
		count[b]++
	}

	for i := 1; i <= n; i++ {
		if count[i] == n-1 {
			return i
		}
	}

	return -1
}
