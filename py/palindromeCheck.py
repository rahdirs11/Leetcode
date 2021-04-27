'''Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.'''

class Solution:
	def isPalindrome(self, s: str) -> bool:
		i, j = 0, len(s) - 1
		palindrome = True
		while i <= j:
			if not s[i].isalnum():
				i += 1
				continue
			if not s[j].isalnum():
				j -= 1
				continue
			if s[i].isalpha() and s[j].isalpha():
				if s[i].lower() == s[j].lower():
					i += 1
					j -= 1
				else:
					return False
			elif s[i].isdigit() and s[j].isdigit():
				if s[i] == s[j]:
					i += 1
					j -= 1
				else:
					return False
			else:
				return False
		return palindrome


print(Solution().isPalindrome(input()))


