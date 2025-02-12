# Changed the method for calculating digit sum (most speed-up), using the built-in heapq culling to implement Priority Queue
class Solution:
    def calculate_digit_sum(self, num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    def maximumSum(self, nums: List[int]) -> int:
        # table record two largest numbers in each sum of digits 
        digits_sum_dt = {}

        for i in range(len(nums)):
            num = nums[i]
            # dig_sum = sum(int(digit) for digit in str(num))
            dig_sum = self.calculate_digit_sum(num)

            # update table
            if dig_sum not in digits_sum_dt:
                digits_sum_dt[dig_sum] = []

            # push in heap
            heapq.heappush(digits_sum_dt[dig_sum], num)
            
            # pop min val if heap exceed 2
            if len(digits_sum_dt[dig_sum]) > 2:
                heapq.heappop(digits_sum_dt[dig_sum])

        # search maximum sum for each sum of digits group
        max_result = -1
        for key in digits_sum_dt.keys():
            if (len(digits_sum_dt[key]) == 2) and (sum(digits_sum_dt[key]) > max_result):
                max_result = sum(digits_sum_dt[key])
        
        return max_result
