class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # build hash map 
        dt = {}
        for i in s:
            if i in dt:
                dt[i] += 1
            else:
                dt[i] = 1
        
        # update hash map & check 
        for i in t:
            if i in dt:
                if dt[i] != 0:
                    dt[i] -= 1
                else:
                    return False
            else:
                return False
        
        return True
