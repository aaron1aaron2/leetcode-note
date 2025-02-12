# Replace the two maximums from using the Priority Queue to save only a single maximum per digit sum, 
# and dynamically compare and replace the global maximum sum with each drop dynamic
class Solution:
    def calculate_digit_sum(self, num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    def maximumSum(self, nums: List[int]) -> int:
        # table record largest numbers in each sum of digits 
        digits_sum_dt = {}
        max_result = -1

        for i in range(len(nums)):
            num = nums[i]
            # dig_sum = sum(int(digit) for digit in str(num))
            dig_sum = self.calculate_digit_sum(num)

            # update table
            if dig_sum not in digits_sum_dt:
                digits_sum_dt[dig_sum] = num
            else:
                curr_digits_sum = digits_sum_dt[dig_sum] + num
                # update largest num
                if num > digits_sum_dt[dig_sum]:
                    digits_sum_dt[dig_sum] = num

                # update max sum
                if curr_digits_sum > max_result:
                    max_result = curr_digits_sum
        
        return max_result
