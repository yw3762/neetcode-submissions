class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)
        for c in charSet:
            count = l = 0 # count c in the window s[l:r+1]
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r-l+1) - count > k: # if used up all k replacements
                    if s[l] == c:          # shrink the window from left
                        count -= 1
                    l += 1
                res = max(res, r-l+1)
        return res