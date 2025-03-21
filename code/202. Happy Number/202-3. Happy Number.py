# use two pointer | space O(1)
class Solution:
    def isHappy(self, n: int) -> bool:    
        
        def get_next_number(n):    
            output = 0
            
            while n:
                digit = n % 10 # 餘數
                output += digit ** 2
                n = n // 10 # 進位捨去餘數
            
            return output
        # slow 1 step、fast 2 step -> 判斷循環的方式
        slow = get_next_number(n)
        fast = get_next_number(get_next_number(n))

        while slow != fast:
            if fast == 1: return True
            slow = get_next_number(slow)
            fast = get_next_number(get_next_number(fast))

        return slow == 1
