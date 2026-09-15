class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t): 
            return False
        count = [0] * 26
        for i in range(n):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for i in range(26):
            if count[i] != 0:
                return False
        return True