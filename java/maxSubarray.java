/*
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-100000]
Output: -100000

(Kadane's Algorithm - with negative numbers!)
*/



import java.io.*;
class Solution {
    public int maxSubArray(int[] nums) {
        int sum = 0, maxSum = -100001;
        // int l = 0, r = -1;
        int maxSubArray = 0;
        for (int i = 0; i < nums.length; ++i) {
            sum += nums[i];
            if (sum > maxSum) {
                // r = i;
                maxSum = sum;
            }
            if (sum < 0) {
                // l = i + 1;
                sum = 0;
            }
        }
        return maxSum;
    }
}