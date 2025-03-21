# my solution | O(log² n)
class Solution:
    def isHappy(self, n: int) -> bool:
        record = [n] # record repeat num
        while n != 1:
            new_n = 0
            for i in str(n):
                new_n += int(i)*int(i)
            n = new_n
            
            if new_n in record:
                # go into circle
                return False
            else:
                record.append(new_n)
        #  find 1
        return True
