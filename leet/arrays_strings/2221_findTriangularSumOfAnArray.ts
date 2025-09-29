// 2221. Find Triangular Sum of an Array

function triangularSum(nums: number[]): number {
    while (nums.length > 1) {
        let tmp = [];
        for (let i = 0; i < nums.length - 1; i++) {
            tmp.push((nums[i] + nums[i + 1]) % 10);
        }
        nums = tmp;
    }
    return nums[0];
}

console.assert(triangularSum([1, 2, 3, 4, 5]) === 8);
console.assert(triangularSum([5]) === 5);
