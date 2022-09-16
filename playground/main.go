package main

import "fmt"

func maximumScore(nums []int, multipliers []int) int {
	var dp [][]int

	// init
	dp = make([][]int, len(multipliers))
	for i, _ := range dp {
		dp[i] = make([]int, len(nums))
	}

	for r := 0; r < len(dp); r++ {
		for c := 0; c < len(dp[0]); c++ {
			dp[r][c] = multipliers[r] * nums[c]
		}
	}

	for i, _ := range dp {
		fmt.Println(dp[i])
	}
	return 1
}

func main() {
	nums := []int{-5, -3, -3, -2, 7, 1}
	multipliers := []int{-10, -5, 3, 4, 6}

	fmt.Println(maximumScore(nums, multipliers))
}
