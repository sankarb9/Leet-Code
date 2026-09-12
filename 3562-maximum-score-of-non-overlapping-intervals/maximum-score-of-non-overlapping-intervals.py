class Solution(object):
    def maximumWeight(self, intervals):
        n = len(intervals)

        # start, end, weight, original index
        arr = []
        for i, (s, e, w) in enumerate(intervals):
            arr.append((s, e, w, i))

        arr.sort()

        import bisect

        starts = [x[0] for x in arr]

        # Next interval must start > current end
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect.bisect_right(starts, arr[i][1])

        # dp[i][k] = (maximum weight, lexicographically smallest indices)
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        def better(a, b):
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            # Same weight -> lexicographically smaller indices
            return a if a[1] < b[1] else b

        for i in range(n - 1, -1, -1):
            for k in range(4):
                # Don't take interval
                skip = dp[i + 1][k]

                # Take interval
                future_weight, future_indices = dp[nxt[i]][k + 1]

                indices = tuple(sorted(
                    (arr[i][3],) + future_indices
                ))

                take = (
                    arr[i][2] + future_weight,
                    indices
                )

                dp[i][k] = better(skip, take)

        return list(dp[0][0][1])