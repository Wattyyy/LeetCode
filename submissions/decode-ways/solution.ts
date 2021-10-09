function numDecodings(s: string): number {
    if (s.length == 1) {
        if (s[0] == "0") {
            return 0;
        }
        else {
            return 1;
        }
    }
    let map = new Proxy({}, {
        get: function(object, property) {
            return object.hasOwnProperty(property) ? object[property] : 0;
        }
    });
    for (let i = 0; i < 26; i++) {
        map[(i + 1).toString()] = 1;
    }
    let dp = new Array(s.length);
    dp[0] = map[s[0]];
    dp[1] = dp[0] * map[s[1]] + map[s[0] + s[1]];
    for (let i=2; i<s.length; i++) {
        dp[i] = dp[i - 1] * map[s[i]] + dp[i - 2] * map[s[i - 1] + s[i]];
    }
    return dp[s.length - 1];
};
