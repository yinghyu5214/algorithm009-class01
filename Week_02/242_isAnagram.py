class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l = [0] * 26
        for i in range(len(s)):
            l[ord(s[i]) - ord('a')] += 1
            l[ord(t[i]) - ord('a')] -= 1
        for char in l:
            if char:
                return False
        return True
