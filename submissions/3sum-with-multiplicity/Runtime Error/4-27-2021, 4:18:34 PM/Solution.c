// https://leetcode.com/problems/3sum-with-multiplicity



int threeSumMulti(int* arr, int arrSize, int target){
    int cnt[101] = {0};
    for (int i=0; i<arrSize; i++){
        cnt[arr[i]] += 1;
    }
    int res = 0;
    for (int i=0; i<arrSize; i++){
        int val = target - arr[i];
        cnt[arr[i]] -= 1;
        for (int j=i+1; j<arrSize; j++){
            cnt[arr[j]] -= 1;
            int val = target - arr[i] - arr[j];
            if ((0 <= val) && (val <= 100)){
                res += cnt[val];
            }
        }
        for (int j=i+1; j<arrSize; j++){
            cnt[arr[j]] += 1;
        }
    }
    return res;

}