'''
Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

You may assume that each input would have exactly one solution and you may not use the same element twice.
'''

from typing import List
class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		i, j = 0, len(numbers) - 1
		result = list()
		while i < j:
			twoSum = numbers[i] + numbers[j]
			if twoSum > target:
				j -= 1
			elif twoSum < target:
				i += 1
			else:
				result.extend([i + 1, j + 1])
				break
		return result


print(Solution().twoSum(list(map(int, input().split())), int(input())))