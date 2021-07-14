// https://leetcode.com/problems/number-of-good-pairs

/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    let i;
    let j;
    let ret = 0;
    for (i = 0; i < nums.length; i++) {
        for (j = i + 1; j < nums.length; j++){
            if (nums[i] == nums[j]){
                ret += 1;
            }
        }
    }
    return ret
    
};