# using heap to improve performance
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # import heapq
        heapq.heapify(nums)

        operations = 0
        min_val = nums[0] # get min val from heap
        while (min_val < k) & (len(nums) >= 2):
            x = heapq.heappop(nums) # Smaller value | equal to min(x,y)
            y = heapq.heappop(nums) # biger value | equal to max(x,y)
            
            # add new number
            heapq.heappush(nums, x*2 + y)

            # update global min val
            min_val = nums[0]

            # count
            operations += 1
        
        return operations
