class Solution {
    public int[] sortArrayByParity(int[] nums) {
        LinkedList<Integer> odds = new LinkedList<>();
        LinkedList<Integer> evens = new LinkedList<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 0) {
                evens.add(nums[i]);
            } else {
                odds.add(nums[i]);
            }
        }
        while (odds.size() > 0) {
            evens.add(odds.removeFirst());
        }
        int[] result = new int[nums.length];
        int i = 0;
        while (evens.size() > 0) {
            result[i] = evens.removeFirst();
            i++;
        }
        return result;
    }
}
