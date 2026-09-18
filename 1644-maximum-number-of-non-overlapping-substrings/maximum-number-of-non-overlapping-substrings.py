class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}

        # Find first and last occurrence
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []

        # Find the smallest valid interval for each character
        for ch in first:
            left = first[ch]
            right = last[ch]
            i = left
            valid = True

            while i <= right:
                c = s[i]

                # This character occurs before our interval
                if first[c] < left:
                    valid = False
                    break

                # Expand interval if needed
                right = max(right, last[c])
                i += 1

            if valid:
                intervals.append((left, right))

        # Greedy: choose intervals ending earliest
        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                ans.append(s[left:right + 1])
                prev_end = right

        return ans