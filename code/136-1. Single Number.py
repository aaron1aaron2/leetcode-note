# simple solution via dict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        record = {}
        for i in nums:
            if i not in record:
                record[i] = ''
            else:
                del record[i]
        
        return list(record.keys())[0]
