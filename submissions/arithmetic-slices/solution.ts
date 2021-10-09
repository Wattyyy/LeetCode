function numberOfArithmeticSlices(nums: number[]): number {
    if (nums.length <= 2) {
        return 0; 
    }
    let dp: Array<number> = new Array(nums.length);
    dp[0] = 1;
    dp[1] = 2;
    let prev_diff = nums[1] - nums[0];
    for (let i = 2; i < nums.length; i++) {
        if (nums[i] - nums[i-1] == prev_diff) {
            dp[i] = dp[i-1] + 1;
        }
        else {
            dp[i] = 2;
        }
        prev_diff = nums[i] - nums[i-1];
    }

    let ans = 0;
    for (let i = 2; i < nums.length; i++) {
        ans += Math.max(dp[i] - 2, 0);
    }
    
    return ans;
};
