class Solution:
	def intToRoman(self, num: int) -> str:
		conversion = {
		1000: 'M',
		900: 'CM',
		500: 'D',
		400: 'CD',
		100: 'C',
		90: 'XC',
		50: 'L',
		40: 'XL',
		10: 'X',
		9: 'IX',
		5: 'V',
		4: 'IV',
		1: 'I'
		}
		temp = num
		roman = str()
		for i, r in conversion.items():
			count = temp // i
			roman += (r * count)

			temp %= i

		return roman

print(Solution().intToRoman(int(input())))