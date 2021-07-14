// https://leetcode.com/problems/count-primes

# include <stdio.h>

int countPrimes(int n) {
    int arr[5000001];
    for (int i = 0; i < 5000001; i++) {
        arr[i] = 1;
    }
    for (int num = 0; num < 5000001; num++) {
        if ((num == 0) || (num == 1)) {
            arr[num] = 0;
        }
        if (arr[num] == 1){
            int i = 2;
            while (num * i <= 5000000) {
                arr[num * i] = 0;
                i += 1;
            }
        }
    }
    
    int res = 0;
    for (int j = 0; j < n + 1; j++) {
        if (arr[j] == 1) {
            res += 1;
        }
    }
    return res;
}