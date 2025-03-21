#  Simply use set to determine if it is the same length | The downside is that there is an additional cost to all nums using sets
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
