class Solution:
    def numDecodings(self, s: str) -> int:
        # for each index, you could choose it as itself a number (if between 1-9)
        # or you could use it as the start of 
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        nums = [int(c) for c in s]
        dp = [0] * len(s)
        dp[0] = 1
        if 10 <= (nums[0] * 10 + nums[1]) <= 26:
            dp[1] = 1
        if nums[1] != 0:
            dp[1] += 1
        for i in range(2, len(s)):
            if 10 <= (nums[i-1] * 10 + nums[i]) <= 26:
                dp[i] += dp[i-2]
            if nums[i] != 0:
                dp[i] += dp[i-1]
        print(dp)
        return dp[-1]