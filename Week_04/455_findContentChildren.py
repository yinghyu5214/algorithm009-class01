class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # s least satisfy g least
        g.sort()
        s.sort()
        i, j = 0, 0
        count = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
            j += 1
        return count

