function countOrders(n: number): number {
    let dp = new Array(n + 1);
    dp[0] = 0;
    dp[1] = 1;
    const MOD = 10 ** 9 + 7;
    for (let i = 2; i < n + 1; i++) {
        dp[i] = (((2 * i) * (2 * i - 1) / 2) * dp[i - 1]) % MOD
    }
    return dp[n];
};
