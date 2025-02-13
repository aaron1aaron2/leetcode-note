# using heap to improve performance
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # import heapq
        heapq.heapify(nums)

        operations = 0
        min_val = nums[0] # get min val from heap
        while (min_val < k) & (len(nums) >= 2):
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            
            # add new number
            heapq.heappush(nums, min([x, y])*2 + max([x, y]))

            # update global min val
            min_val = nums[0]

            # count
            operations += 1
        
        return operations
