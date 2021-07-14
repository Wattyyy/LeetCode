// https://leetcode.com/problems/count-primes

# include <math.h>
# include <stdio.h>

int isPrime(int num) {
    if (num <= 1) {
        return 0;
    }
    if ((num == 2) || (num == 3)) {
        return 1;
    }
    int end = sqrt(num);
    int d;
    for (d=2; d<=end+1; d++) {
        if (num % d == 0) {
            return 0;
        }
    }
    return 1;
}

int countPrimes(int n) {
    int res = 0;
    int i;
    for (i=0; i<n; i++) {
        if (isPrime(i) == 1) {
            res += 1;
        }
    }
    return res;

}