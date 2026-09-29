class Solution(object):
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 == 1:
            return False

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]

        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):

                for balance in dp[i][j]:
                    # Move down
                    if i + 1 < m:
                        new_balance = balance + (1 if grid[i + 1][j] == '(' else -1)
                        if new_balance >= 0:
                            dp[i + 1][j].add(new_balance)

                    # Move right
                    if j + 1 < n:
                        new_balance = balance + (1 if grid[i][j + 1] == '(' else -1)
                        if new_balance >= 0:
                            dp[i][j + 1].add(new_balance)

        return 0 in dp[m - 1][n - 1]