class Solution {
	public int dominantIndex(int[] nums) {
		int maxElement = Integer.MIN_VALUE, maxElementIndex = -1;
		for (int i = 0; i < nums.length; ++i) {
			if (maxElement <= nums[i]) {
				maxElement = nums[i];
				maxElementIndex = i;
				// System.out.println();
			}
		}
		for (int n: nums) {
			if (n == maxElement) {
				continue;
			}
			if (!(n * 2 <= maxElement)) {
				return -1;
			}
		}
		return maxElementIndex;
	}

	public static void main(String[] args) {
		Solution obj = new Solution();
		System.out.println(obj.dominantIndex(new int[]{1, 2, 3, 4}));
	}
}