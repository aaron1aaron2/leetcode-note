# simple hashmap solution using dict | O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        match_dt = {} # {num: idx}
        for idx, num in enumerate(nums):
            match_num = target - num
            if match_num in match_dt:
                return [match_dt[match_num], idx]
            else:
                match_dt[num] = idx
