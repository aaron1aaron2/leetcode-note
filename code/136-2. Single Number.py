# solution by https://leetcode.com/problems/single-number/solutions/6026000/0-ms-runtime-beats-100-user-step-by-steps-solution-easy-to-understand/
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
