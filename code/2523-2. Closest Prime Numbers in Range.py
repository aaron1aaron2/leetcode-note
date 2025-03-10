# Prime number judgment optimization, in the number i of 5 ~ n, only search for the number of i*i < n
# O(n∗sqrt(n))
class Solution:
    def is_prime(self, n:int) -> bool:
        '''
        1. We just need to check sqrt(n), because if n has a factor 
        greater than sqrt(n), then it must also have a factor less than 
        sqrt(n).
        2. We checked at intervals of 6, because all prime numbers are
        shaped like 6k ± 1 (except 2 and 3)
        '''
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
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
