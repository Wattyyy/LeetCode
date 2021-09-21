/**
 * @param {number[]} cost
 * @return {number}
 */
 var minCostClimbingStairs = function(cost) {
    let N = cost.length;
    if (N == 2) {
        return Math.min(cost[0], cost[1]);
    }
    let dp = new Array(N);
    dp[0] = cost[0];
    dp[1] = cost[1];
    for (let i=2; i<N; i++){
        dp[i] = Math.min(dp[i-2], dp[i-1]) + cost[i];
    }
    return Math.min(dp[N-1], dp[N-2]);
};
