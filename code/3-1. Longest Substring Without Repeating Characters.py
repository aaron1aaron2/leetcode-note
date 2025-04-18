class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length_max = 1 if (len(s) != 0) else 0 # handle edge case

        left = 0
        right = 1
        # When the right side has reached the bottom, there will be no longer strings subsequently
        while right < len(s):
            if s[right] not in s[left:right]:
                right += 1
                if (right - left) > length_max:
                    length_max = (right - left) 
            else:
                left += 1

        return length_max
        
