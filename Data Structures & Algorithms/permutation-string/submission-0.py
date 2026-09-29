class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        k = len(s1)
        target = [0] * 26
        window = [0] * 26
        base = ord('a')
        
        for c in s1:
            target[ord(c) - base] += 1

        for right, c in enumerate(s2):
            window[ord(c) - base] += 1

            if right >= k:
                window[ord(s2[right - k]) - base] -= 1

            if right >= k-1 and window == target:
                return True

        return False