'''You are given an array prices for which the ith element is the price of a given stock on day i.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).'''
from typing import List
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		buy, sell = prices[0], prices[0]
		result = 0
		for i in range(1, len(prices)):
			if prices[i] > sell:
				sell = prices[i]
			else:
				result += sell - buy
				buy, sell = prices[i], prices[i]
		result += sell - buy
		return result
		

print(Solution().maxProfit(list(map(int, input().split()))))