// 53. Maximum Subarray
function maxSubArray(nums: number[]): number {
    let maxSum = nums[0];
    let currSum = 0;
    for (let n of nums) {
        // if currSum drops below zero -> change its value to zero
        // i.e. discard the value we've aggregated so far and start fresh
        currSum = Math.max(currSum, 0) + n;
        maxSum = Math.max(maxSum, currSum);
    }

    return maxSum;
}

function maxSubArray_alt(nums: number[]): number {
    let maxSum = nums[0];
    let currSum = 0;
    for (let n of nums) {
        currSum = Math.max(n, currSum + n);
        maxSum = Math.max(maxSum, currSum)
    }
    return maxSum;
}


const maxSubArrayCases = [
    { nums: [-2, 1, -3, 4, -1, 2, 1, -5, 4], result: 6 },
    { nums: [1], result: 1 },
    { nums: [5, 4, -1, 7, 8], result: 23 },
    { nums: [-1], result: -1 },
    { nums: [-2, -1], result: -1 },
];

maxSubArrayCases.forEach(({ nums, result }) => {
    const actual = maxSubArray(nums);
    console.assert(actual === result, `${actual} !== ${result}`);
});
