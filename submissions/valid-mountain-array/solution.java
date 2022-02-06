class Solution {
    public boolean validMountainArray(int[] arr) {
        if (arr.length <= 2) {
            return false;
        }
        
        boolean climbing;
        boolean changed = false;
        if (arr[0] < arr[1]) {
            climbing = true;
        }
        else {
            return false;
        }

        for (int i=2; i < arr.length; i++) {
            if ((climbing && arr[i-1] < arr[i]) || (!climbing && arr[i-1] > arr[i])) {
                continue;
            }
            else if (climbing && arr[i-1] > arr[i]) {
                climbing = !climbing;
            }
            else {
                return false;
            }
        }

        if (!climbing) {
            return true;
        }
        else {
            return false;
        }
    }
}
