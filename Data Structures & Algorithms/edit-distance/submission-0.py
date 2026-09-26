class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        if l1 > l2: return self.minDistance(word2, word1)

        dp = [[i for i in range(l1 + 1)], [0 for _ in range(l1 + 1)]]
        
        for j in range(1, l2 + 1):
            for i in range(l1 + 1):
                curr_id = j % 2
                prev_id = (curr_id - 1) % 2
                if i == 0:
                    dp[curr_id][i] = j
                elif word1[i-1] == word2[j-1]:
                    dp[curr_id][i] = dp[prev_id][i-1]
                else:
                    dp[curr_id][i] = min (
                        dp[curr_id][i-1] + 1,    # delete
                        dp[prev_id][i] + 1,     # insert
                        dp[prev_id][i-1] + 1    # replace
                    )
        return dp[l2 % 2][l1]