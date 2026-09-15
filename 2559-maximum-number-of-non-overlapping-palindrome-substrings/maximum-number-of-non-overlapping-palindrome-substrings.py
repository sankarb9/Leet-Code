class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # dp[i] = maximum palindromes using first i characters
        dp = [0] * (n + 1)

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(k, n + 1):

            # Don't use a palindrome ending at i-1
            dp[i] = dp[i - 1]

            # Check palindrome of length k
            if isPalindrome(i - k, i - 1):
                dp[i] = max(dp[i], dp[i - k] + 1)

            # Check palindrome of length k + 1
            if i - k - 1 >= 0:
                if isPalindrome(i - k - 1, i - 1):
                    dp[i] = max(dp[i], dp[i - k - 1] + 1)

        return dp[n]