from collections import deque

class Solution:
	def maxSlidingWindow(self, nums, k: int):
		queue = deque([])
		result = []
		for i in range(len(nums)):
			if queue and i - queue[0] >= k:
				queue.popleft()
			
			while queue and nums[queue[-1]] < nums[i]:
				queue.pop()
		
			queue.append(i)
			result.append(nums[queue[0]])
		return result[k - 1: ]


