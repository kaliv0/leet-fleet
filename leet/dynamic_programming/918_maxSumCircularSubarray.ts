// 918. Maximum Sum Circular Subarray
function maxSubarraySumCircular(nums: number[]): number {
    let totalSum = 0;
    let maxSum = nums[0];
    let minSum = nums[0];
    let currMax = 0;
    let currMin = 0;
    for (let n of nums) {
        // Kadane's max
        currMax = Math.max(currMax, 0) + n;
        maxSum = Math.max(maxSum, currMax);
        // Kadane's min
        currMin = Math.min(currMin, 0) + n;
        minSum = Math.min(minSum, currMin);

        totalSum += n;
    }

    if (totalSum === minSum) {
        // if all numbers are negative -> return their sum instead of zero
        return maxSum;
    }

    // return either maxSum (inside array) or circularSum (made of subarrays form both sides)
    return Math.max(maxSum, totalSum - minSum);
}

const maxSubarraySumCircularCases = [
    { nums: [1, -2, 3, -2], result: 3 },
    { nums: [5, -3, 5], result: 10 },
    { nums: [-3, -2, -3], result: -2 },
];

maxSubarraySumCircularCases.forEach(({ nums, result }) => {
    const actual = maxSubarraySumCircular(nums);
    console.assert(actual === result, `${actual} !== ${result}`);
});
