class Solution:
    def myAtoi(self, s: str) -> int:
        # import sys
        word = s.strip().split()[0]
        number = 0
        sign = '-' if word[0] == '-' else ''
        word = word[1: ] if word[0] in ['+', '-'] else word
        i = 0
        if word[0] == '.':
            return 0
        isValid = True
        while i < len(word):
            if word[i] == '.':
                break
            if not word[i].isdigit():
                isValid = False
                break
            i += 1

        if isValid:
            word = word[: i]
            # print(word)
            number = int(word)
            if sign == '-':
                return -2 ** 31 if -number < -2 ** 31 else -number
            else:
                return 2 ** 31 - 1 if number > 2 ** 31 - 1 else number
        else:
            return 0

print(Solution().myAtoi(input()))