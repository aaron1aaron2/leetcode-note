# 使用 set 代替 list 儲存資料，以供查詢 | O(logn)
class Solution:
    def isHappy(self, n: int) -> bool:
        record = {n}  # 使用 set
        while n != 1:
            new_n = 0
            for i in str(n):
                new_n += int(i) * int(i)
            n = new_n
            if new_n in record:
                return False
            record.add(new_n)
        return True
