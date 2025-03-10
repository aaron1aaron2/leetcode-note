# using Sieve of Eratosthenes | O(right * log(log(right)))
class Solution:
    def get_primes(self, n:int) -> bool:
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n + 1, i):
                    sieve[j] = False

        return sieve

    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Gets all prime numbers from left to right
        primes_of_n = self.get_primes(right) 
        primes = [i for i in range(left, right + 1) if primes_of_n[i]]

        # Search closer prime 
        min_pair = [-1, -1]
        min_val = right - left + 1 
        prev_prime = None
        for i in primes:
            if prev_prime:
                cur_val = i - prev_prime

                if cur_val < min_val:
                    min_val = cur_val
                    min_pair = [prev_prime, i]
                
            prev_prime = i

        return min_pair
