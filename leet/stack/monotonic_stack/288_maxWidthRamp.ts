// 962. Maximum Width Ramp

function maxWidthRamp_bruteForce(nums: number[]): number {
    // exceeds time limit
    let maxWidth = 0;
    for (let i = 0; i < nums.length - 1; i++) {
        for (let j = 0; j < nums.length; j++) {
            if (nums[i] <= nums[j]) {
                maxWidth = Math.max(maxWidth, j - i);
            }
        }
    }

    return maxWidth;
}

function maxWidthRamp(nums: number[]): number {
    // fill monotic stack of indeces in desc order (by value)
    const indecesStack: number[] = [];
    for (let i = 0; i < nums.length; i++) {
        if (!indecesStack.length || nums[i] < nums[indecesStack[indecesStack.length - 1]]) {
            indecesStack.push(i);
        }
    }

    // traverse backwwards from the right side and scan for maxWidth pair
    let maxWidth = 0;
    for (let j = nums.length - 1; j >= 0; j--) {
        while (indecesStack && nums[j] >= nums[indecesStack[indecesStack.length - 1]]) {
            maxWidth = Math.max(maxWidth, j - indecesStack[indecesStack.length - 1]);
            indecesStack.pop();
        }
    }

    return maxWidth;
}

console.assert(maxWidthRamp([6, 0, 8, 2, 1, 5]) == 4);
console.assert(maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7);
