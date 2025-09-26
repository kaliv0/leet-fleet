// 16. 3Sum Closest

function threeSumClosest(nums: number[], target: number): number {
    nums.sort((a, b) => a - b);

    let result = Number.MAX_VALUE;
    for (let i = 0; i < nums.length - 2; i++) {
        let j = i + 1;
        let k = nums.length - 1;

        while (j < k) {
            const curr_sum = nums[i] + nums[j] + nums[k];
            if (Math.abs(target - curr_sum) < Math.abs(target - result)) {
                result = curr_sum;
            }

            if (curr_sum < target) {
                j++;
            } else {
                k--;
            }
        }
    }

    return result;
}

const cases = [
    { nums: [-1, 2, 1, -4], target: 1, result: 20 },
    { nums: [0, 0, 0], target: 1, result: 0 },
    { nums: [1, 2, 7, 13], target: 12, result: 10 },
];

cases.forEach(({ nums, target, result }) => {
    const actual = threeSumClosest(nums, target);
    console.assert(actual === result, `${actual} !== ${result}`);
});
