	class Solution:
		def singleNumber(self, nums) -> int:
			xor = 0
			for n in nums:
				xor ^= n

			return xor
		