class Solution:
	def climbStairs(self, n: int, dp: dict={}) -> int:
		if n in dp:
			return dp[n]
		if n < 0:
			return 0
		if n == 0:
			return 1
		dp[n] = self.climbStairs(n - 2, dp) + self.climbStairs(n - 1, dp)
		return dp[n]


print(Solution().climbStairs(int(input())))