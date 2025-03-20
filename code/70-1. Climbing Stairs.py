class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1) # to save ways to each step

        dp[0] = 1
        dp[1] = 1
        # The number of update methods is progressively increased from small to large
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]
