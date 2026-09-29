from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        need = Counter(t)
        missing = len(t)
        best_len = float('inf')
        best_left = 0


        for right, c in enumerate(s):
            # add c into the counter
            if need[c] > 0:
                missing -= 1
            need[c] -= 1


            while missing == 0:
                # Record before shrinking
                size = right - left + 1
                if size < best_len:
                    best_len = size
                    best_left = left

                # Remove outgoing character
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        if best_len == float('inf'):
            return ""
        return s[best_left:best_left + best_len]
            