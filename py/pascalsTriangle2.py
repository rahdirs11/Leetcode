'''
Pascals Triangle, return the rowIndex th value in the triangle (0-based index)
'''


from typing import List

class Solution:
	def generate(self, rowIndex: int) -> List[List[int]]:
		# triangle = []
		# curr = [1]
		i = 0
		while i <= rowIndex:
			if i == 0:
				# triangle.append([1])
				curr = [1]
			elif i == 1:
				# triangle.append([1, 1])
				curr = [1, 1]
			else:
				# prevRow = triangle[i - 1][:]
				prevRow = curr
				row = [1, 1]
				j = 0
				pairs, index = 0, 1
				while j < i - 1 and pairs < len(prevRow) - 1:
					row.insert(j + 1, prevRow[pairs] + prevRow[pairs + 1])
					j += 1
					pairs += 1
				# triangle.append(row)
				curr = row
			i += 1
		# return triangle
		return curr

print(Solution().generate(int(input())))
# for row in Solution().generate(int(input())):
# 	print(row)
