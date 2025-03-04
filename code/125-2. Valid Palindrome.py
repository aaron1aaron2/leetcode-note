# Think about it from another perspective and directly determine whether the string is consistent after flipping | by solution -> https://leetcode.com/problems/valid-palindrome/solutions/6235854/easy-approach-solution-simple-please-upvote/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = "".join([char.lower() for char in s if char.isalnum()])
    
        return check == check[::-1]
