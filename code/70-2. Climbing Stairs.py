# by https://leetcode.com/problems/climbing-stairs/solutions/6162936/dynamic-programming-solution/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        prev1 = 2
        prev2 = 1
        cur = prev1 + prev2

        for _ in range(2, n):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur
        
        return cur
