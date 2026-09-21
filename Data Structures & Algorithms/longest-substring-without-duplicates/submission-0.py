class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        lo = 0
        seen = {s[lo]}
        max_len = 1
        for i in range(1, len(s)):
            while s[i] in seen:
                seen.discard(s[lo])
                lo += 1
            seen.add(s[i])
            max_len = max(i - lo + 1, max_len)
        return max_len

