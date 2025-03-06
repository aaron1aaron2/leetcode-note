# use hash table
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) # n*n matrix
        last_num = n*n

        record_dt = {i:'' for i in range(1,last_num+1)}
        i, j = 0, 0
        for i in range(n):
            for j in range(n):
                num = grid[i][j]
                if num in record_dt:
                    del record_dt[num]
                else:
                    repeat = num

        miss = list(record_dt.keys())[0]

        return repeat, miss
