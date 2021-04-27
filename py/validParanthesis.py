'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchOpen = {')': '(', '}': '{', ']': '['}
        for b in s:
            if b in ['(', '{', '[']:
                stack.append(b)
            else:
                if len(stack) != 0 and stack[-1] == matchOpen.get(b):
                    stack.pop()
                else:
                    return False
        return not len(stack)
        