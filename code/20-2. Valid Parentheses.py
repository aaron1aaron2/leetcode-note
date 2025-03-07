# using stack 
class Solution:
    def isValid(self, s: str) -> bool:
        record_stack = []
        close__dt = {
            ')':'(', '}':'{', ']':'['
        }
        for i in s:
            if i in close__dt.keys():
                # when close
                get_prev = record_stack.pop() if (len(record_stack) != 0) else None
                if get_prev != close__dt[i]:
                    return False
            else:
                record_stack.append(i)
        
        if len(record_stack) == 0:
            return True
        else:
            return False
