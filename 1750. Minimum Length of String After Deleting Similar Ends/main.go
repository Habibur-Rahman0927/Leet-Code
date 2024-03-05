package main

func main() {
    input := "aabccabba"
    result := minimumLength(input)
    fmt.Println(result) // Output: 2
}

func minimumLength(s string) int {
    l, r := 0, len(s)-1

    for l < r && s[l] == s[r] {
        tmp := s[l]
        for l <= r && s[l] == tmp {
            l++
        }
        for l <= r && s[r] == tmp {
            r--
        }
    }
    return (r - l + 1)
}