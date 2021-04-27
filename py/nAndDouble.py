from typing import List

class Solution:
	def checkIfExist(self, arr: List[int]) -> bool:
		# for i in range(len(arr)):
		# 	for j in range(len(arr)):
		# 		if i != j and arr[i] * 2 == arr[j]:
		# 			return True
		# return False
		'''above solution is O(n ^ 2)'''
		d = {}
		for i, num in enumerate(arr):
			if num not in d:
				d[num] = i

		for i, num in enumerate(arr):
			if num * 2 in d and d[num * 2] != i:
				return True

		return False
		# and this is O(2n) => O(n), space = O(n)




print(Solution().checkIfExist(list(map(int, input().split()))))