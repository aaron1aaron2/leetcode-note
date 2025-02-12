class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # Track current lengths of increasing and decreasing sequences
        incread_max_len = 1
        decread_max_len = 1

        # Track current max lengths
        final_max_len = 1

        for i in range(len(nums) - 1):
            # Each position is judged to increase, decrease or remain unchanged
            if nums[i + 1] > nums[i]:
                decread_max_len += 1
                incread_max_len = 1
            elif nums[i + 1] < nums[i]:
                incread_max_len += 1
                decread_max_len = 1
            else:
                decread_max_len = 1
                incread_max_len = 1

            # Record the best result now
            final_max_len = max(final_max_len, incread_max_len, decread_max_len)

        return final_max_len
