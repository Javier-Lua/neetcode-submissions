class Solution:
    # Can redo, because there is a solution with only right!
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding window of size 2
        # left keeps track of smallest number
        # left and right moves together
        # calculate profit at every step
        if len(prices) < 2:
            return 0
        left = 0
        curr_min = prices[left]
        right = 1
        curr_profit = prices[right] - prices[left]
        max_profit = curr_profit
        while right < len(prices) - 1:
            left += 1
            right += 1
            curr_min = min(curr_min, prices[left])
            curr_profit = prices[right] - curr_min
            max_profit = max(max_profit, curr_profit)
        return max(0, max_profit)
