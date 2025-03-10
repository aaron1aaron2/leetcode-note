# Time Limit Exceeded 
class Solution:
    def is_prime(self, num:int) -> bool:
        if num == 1:
            return False

        for i in range(2,num):
            if num % i == 0:
                return False
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:
        min_val = right - left + 1 # Make sure it is greater than all the values in the range
        min_pair = [-1, -1]
        prev_prime = None
        for i in range(left, right+1):
            if self.is_prime(i):
                if prev_prime:
                    cur_val = i - prev_prime

                    if cur_val < min_val:
                        min_val = cur_val
                        min_pair = [prev_prime, i]
                
                prev_prime = i

        return min_pair
