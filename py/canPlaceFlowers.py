from typing import List

class Solution:
	def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
		i = 0
		while i < len(flowerbed):
			if not flowerbed[i]:
				if i + 1 < len(flowerbed):
					if not flowerbed[i + 1]:
						n -= 1
						i += 2
					else:
						i += 3
				else:
					n -= 1
					i += 1
			else:
				i += 2
		return n <= 0


print(Solution().canPlaceFlowers(list(map(int, input().split())), int(input())))