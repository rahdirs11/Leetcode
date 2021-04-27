def lengthOfLastWord(string: str) -> int:
	words = string.split()
	return len(words[-1]) if len(words) != 0 else 0

print(lengthOfLastWord(input()))