# Time Limit Exceeded | filter prime num O(n) -> sort prime num O(m) -> search min diff O(m)
class Solution:
    def is_prime(self, num:int) -> bool:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime_nums = []
        for i in range(left, right+1):
            if is_prime(i):
                prime_nums.append(i)

        if len(prime_nums) > 1:
            prime_nums = sorted(prime_nums)   
            min_pair = [prime_nums[0], prime_nums[1]]
            min_val = prime_nums[1] - prime_nums[0]
            for i in range(len(prime_nums)-1):
                cur_val = prime_nums[i+1] - prime_nums[i]
                if cur_val < min_val:
                    min_val = cur_val
                    min_pair = [prime_nums[i], prime_nums[i+1]]

            return min_pair
        else:
            return [-1, -1]
            

        

        
