// 1. Two Sum

package main

import (
	"fmt"
	"reflect"
)

func twoSum(nums []int, target int) []int {
	var indices = make(map[int]int)
	for idx, curr := range nums {
		if compIdx, ok := indices[target-curr]; ok {
			return []int{compIdx, idx}
		}
		indices[curr] = idx
	}
	return nil
}

func main() {
	for _, test := range []struct {
		nums   []int
		target int
		want   []int
	}{
		{[]int{2, 7, 11, 15}, 9, []int{0, 1}},
		{[]int{3, 2, 4}, 6, []int{1, 2}},
		{[]int{3, 3}, 6, []int{0, 1}},
	} {
		got := twoSum(test.nums, test.target)
		if !reflect.DeepEqual(got, test.want) {
			fmt.Printf("twoSum(%v, %d) = %v; want %v\n", test.nums, test.target, got, test.want)
		}
	}
}
