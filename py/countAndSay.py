class Solution:
	def countAndSay(self, n: int) -> str:
		if n == 1:	return "1"
		value = self.countAndSay(n - 1)
		string, i = str(), 0
		while i < len(value):
			j, count, charToBeCounted = i + 1, 1, value[i]
			while j < len(value) and charToBeCounted == value[j]:
				j += 1
				count += 1
			string += str(count) + charToBeCounted
			i = j
		return string


if __name__ == "__main__":
	obj = Solution()
	print(obj.countAndSay(int(input())))
