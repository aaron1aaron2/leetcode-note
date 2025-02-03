class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incread_max_len = 1
        decread_max_len = 1
        final_max_len = 1

        pointer = 0
        tmp_len = 1
        length = len(nums)

        if length==1:
            return 1

        for i in nums:
            if pointer < length-1:
                if i > nums[pointer+1]:
                    decread_max_len += 1
                    incread_max_len = 1
                elif i < nums[pointer+1]:
                    incread_max_len += 1
                    decread_max_len = 1
                else:
                    decread_max_len = 1
                    incread_max_len = 1

            final_max_len = max(final_max_len, incread_max_len, decread_max_len)
            pointer += 1

        return final_max_len
