class Solution:
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7

        dp = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')

            # New subsequences formed by adding ch
            new = 1 + sum(dp)

            dp[i] = new % MOD

        return sum(dp) % MOD