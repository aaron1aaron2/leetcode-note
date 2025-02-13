# my initial solution but Time Limit Exceeded.
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        min_val = k-1 # assign initial value smaller than k
        while min_val < k:
            new_nums = []
            min_two = sorted(nums[:2]) # assign first two item as initial value 

            # Compare and replace the smallest two numbers
            for i in range(2, len(nums)):
                if nums[i] < min_two[1]:
                    new_nums.append(min_two[1])
                    min_two[1] = nums[i]
                else:
                    new_nums.append(nums[i])

                min_two = sorted(min_two)
            
            # update global min val
            min_val = min(min_two)

            # add new number
            new_nums.append(min_val*2 + max(min_two))
            
            # replace nums 
            nums = new_nums

            # count
            operations += 1
        
        return operations - 1



        
