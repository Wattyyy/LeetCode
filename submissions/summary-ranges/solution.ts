function summaryRanges(nums: number[]): string[] {
    if (nums.length === 0) {
        return [];
    }
    let tmp: Array<number> = [nums[0]];
    let ans: Array<string> = [];
    for (let i = 1; i < nums.length; i++) {
        if (tmp[tmp.length - 1] + 1 === nums[i]) {
            tmp.push(nums[i]);
        }
        else {
            if (tmp.length === 1) {
                ans.push(tmp[0].toString());
            }
            else {
                let str = tmp[0] + "->" + tmp[tmp.length - 1];
                ans.push(str);
            }
            tmp = [nums[i]];
        }
    }
    
    if (tmp.length === 1) {
        ans.push(tmp[0].toString());
    }
    else if (2 <= tmp.length) {
        let str = tmp[0] + "->" + tmp[tmp.length - 1];
        ans.push(str);
    }
    return ans;
};
