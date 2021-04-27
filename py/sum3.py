from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2:
            return []
        output = []
        nums.sort()
        # for i in range(len(nums)):
        #     j = i + 1
        #     while j < len(nums):
        #         k = j + 1
        #         while k < len(nums):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 sum3 = sorted([nums[i], nums[j], nums[k]])
        #                 if sum3 not in output:
        #                     output.append(sum3)
        #             k += 1
        #         j += 1
        for index, num in enumerate(nums):
            if index > 0 and num == nums[index - 1]:
                continue

            l, r = index + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    output.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return output

print(Solution().threeSum([-1,0,1,2,-1,-4]))