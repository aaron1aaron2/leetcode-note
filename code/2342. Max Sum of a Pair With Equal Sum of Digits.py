class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # table record two largest numbers in each sum of digits 
        digits_sum_dt = {}

        for i in range(len(nums)):
            num = nums[i]
            dig_sum = sum(int(digit) for digit in str(num))

            # update table
            if dig_sum not in digits_sum_dt:
                digits_sum_dt[dig_sum] = [num]
            elif len(digits_sum_dt[dig_sum]) == 1:
                digits_sum_dt[dig_sum].append(num)
            else:
                curr_larg_nums = sorted(digits_sum_dt[dig_sum])
                if curr_larg_nums[0] < num:
                    curr_larg_nums[0] = num
                
                digits_sum_dt[dig_sum] = curr_larg_nums

        # search maximum sum for each sum of digits group
        max_result = -1
        for key in digits_sum_dt.keys():
            if (len(digits_sum_dt[key]) == 2) and (sum(digits_sum_dt[key]) > max_result):
                max_result = sum(digits_sum_dt[key])
        
        return max_result
