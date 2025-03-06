class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_prices = prices[0]
        max_profit = 0 
        
        # Note that if you are looking for the maximum difference, the default maximum value cannot be 0. In this question, it's because he only needs to make a profit.

        for p in prices[1:]: 
            if p < buy_prices:
                buy_prices = p
            
            curr_profit = p - buy_prices
            if curr_profit > max_profit:
                max_profit = curr_profit
        
        return max_profit
            
