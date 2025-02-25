# Because the length is not very long in terms of conditions, you can use the method of trying to use brute force search to solve it
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        length = len(pattern) # <= 8
        from itertools import permutations
        all_results = permutations(range(1, 10), length+1) # get all permutations using python built-in itertools tool

        # By default, the order is sorted by number size, so we can directly compare from small to large in order, without having to sort it anymore
        for seq in all_results:
            seq_str = ''.join([str(i) for i in seq])
            result = self.check_pattern(seq, pattern)

            if result:
                return seq_str
    
    def check_pattern(self, seq: str, pattern: str) -> bool:
        # if part od seq not match return false
        for idx, pat in enumerate(pattern):
            if pat == 'I':
                if seq[idx] > seq[idx+1]:
                    return False
            else:
                if seq[idx] < seq[idx+1]:
                    return False
        
        # when whole seq is pass, return true
        return True
        
