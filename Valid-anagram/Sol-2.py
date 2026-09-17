class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = [0] * 26

        for i in s:
            x[ord(i)-ord('a')] += 1
        for i in t:
            x[ord(i)-ord('a')] -=1
        return x == [0]*26