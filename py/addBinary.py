class Solution:
    def addBits(self, a, b):
        if a != b:
            return (1, 0)
        else:
            return (0, 1) if a and b else (0, 0)

    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = ('0' * (len(b) - len(a))) + a
        elif len(b) < len(a):
            b = ('0' * (len(a) - len(b))) + b        
        carry = 0
        carry2 = 0
        output = str()
        i = len(a) - 1
        while i > -1:
            if carry:
                val, carry2 = self.addBits(int(a[i]), carry)
                val, carry = self.addBits(int(b[i]), val)
                carry = carry2 or carry
            else:
                val, carry = self.addBits(int(a[i]), int(b[i]))
            output = str(val) + output
            i -= 1
        if carry:
            output = '1' + output
        return output
        


print(Solution().addBinary(input(), input()))
        