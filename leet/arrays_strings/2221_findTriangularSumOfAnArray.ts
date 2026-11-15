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

const triangularSumCases = [
    { nums: [1, 2, 3, 4, 5], result: 8 },
    { nums: [5], result: 5 },
];

triangularSumCases.forEach(({ nums, result }) => {
    const actual = triangularSum(nums);
    console.assert(actual === result, `${actual} !== ${result}`);
});
