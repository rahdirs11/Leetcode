/*
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0
*/

import java.util.Scanner;
class Solution {
    public static int searchInsert(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int mid = l + ((r - l) / 2);
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                if (l == r) {
                    return l;
                } else {
                    r = mid - 1;
                }
            } else {
                if (l == r) {
                    return r + 1;
                } else {
                    l = mid + 1;
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] nums = {1, 3, 5, 6};
        int[] nums2 = {1};
        System.out.println("Position:\t" + searchInsert(nums, 2));
        System.out.println("Position:\t" + searchInsert(nums, 7));
        System.out.println("Position:\t" + searchInsert(nums, 5));
        System.out.println("Position:\t" + searchInsert(nums2, 0));

    }
}