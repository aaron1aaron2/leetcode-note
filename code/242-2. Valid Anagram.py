# solution by https://leetcode.com/problems/valid-anagram/solutions/3687854/3-method-s-c-java-python-beginner-friendly/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t
