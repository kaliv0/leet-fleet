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

console.assert(threeSumClosest([-1, 2, 1, -4], 1) === 2);
console.assert(threeSumClosest([0, 0, 0], 1) === 0);
console.assert(threeSumClosest([1, 2, 7, 13], 12) === 10);
