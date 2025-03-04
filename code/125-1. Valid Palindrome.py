# use two pointer to scan and check each char is match 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # extract char first
        chars = "".join([char.lower() for char in s if char.isalnum()])
        # use two point to scan string
        fw_pointer = 0
        bw_pointer = len(chars) - 1

        while fw_pointer < bw_pointer:
            # check char pairs，if not match returm false
            if chars[fw_pointer] != chars[bw_pointer]:
                return False
            else:
                fw_pointer += 1
                bw_pointer -= 1

        # only Non-letter in input string
        if (len(chars)==0) & (len(chars) == len(s)):
            return False

        return True
