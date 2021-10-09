/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let dp = new Array(nums.length);
    dp[0] = nums[0];
    let ans = nums[0];
    for (i = 1; i < nums.length; i++) {
        dp[i] = Math.max(dp[i - 1] + nums[i], nums[i]);
        ans = Math.max(dp[i], ans);
    }
    return ans
};
