'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it
'''


from typing import List

class Solution:
	def generate(self, numRows: int) -> List[List[int]]:
		triangle = []
		i = 0
		while i < numRows:
			if i == 0:
				triangle.append([1])
			elif i == 1:
				triangle.append([1, 1])
			else:
				prevRow = triangle[i - 1][:]
				row = [1, 1]
				j = 0
				pairs, index = 0, 1
				while j < i - 1 and pairs < len(prevRow) - 1:
					row.insert(j + 1, prevRow[pairs] + prevRow[pairs + 1])
					j += 1
					pairs += 1
				triangle.append(row)
			i += 1
		return triangle


for row in Solution().generate(int(input())):
	print(row)
