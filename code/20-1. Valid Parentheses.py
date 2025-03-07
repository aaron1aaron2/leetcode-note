# No need to comply with first-in, first-out | allow "([)]"
class Solution:
    def isValid(self, s: str) -> bool:
        open_count_dt = {
            '(':0, '{':0, '[':0
        }
        close__dt = {
            ')':'(', '}':'{', ']':'['
        }

        for i in s:
            if i in open_count_dt:
                # when encounter open bracket
                open_count_dt[i] += 1
            else:
                # when encounter close bracket
                open_count_dt[close__dt[i]] -= 1
        
        for i in open_count_dt.keys():
            if open_count_dt[i] != 0:
                return False
        
        return True
