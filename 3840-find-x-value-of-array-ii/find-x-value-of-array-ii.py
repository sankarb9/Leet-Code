from typing import List


class Node:
    def __init__(self, k):
        self.prod = 1
        self.cnt = [0] * k


class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree = [Node(k) for _ in range(4 * self.n)]

        self.build(1, 0, self.n - 1, nums)

    def merge(self, left, right):
        node = Node(self.k)

        # Product of entire segment
        node.prod = (left.prod * right.prod) % self.k

        # Prefixes completely inside left
        for r in range(self.k):
            node.cnt[r] += left.cnt[r]

        # Prefixes that use all of left + prefix of right
        for r in range(self.k):
            new_r = (left.prod * r) % self.k
            node.cnt[new_r] += right.cnt[r]

        return node

    def build(self, idx, l, r, nums):
        if l == r:
            value = nums[l] % self.k

            self.tree[idx].prod = value
            self.tree[idx].cnt[value] = 1
            return

        mid = (l + r) // 2

        self.build(idx * 2, l, mid, nums)
        self.build(idx * 2 + 1, mid + 1, r, nums)

        self.tree[idx] = self.merge(
            self.tree[idx * 2],
            self.tree[idx * 2 + 1]
        )

    def update(self, idx, l, r, pos, value):
        if l == r:
            value %= self.k

            self.tree[idx] = Node(self.k)
            self.tree[idx].prod = value
            self.tree[idx].cnt[value] = 1
            return

        mid = (l + r) // 2

        if pos <= mid:
            self.update(idx * 2, l, mid, pos, value)
        else:
            self.update(idx * 2 + 1, mid + 1, r, pos, value)

        self.tree[idx] = self.merge(
            self.tree[idx * 2],
            self.tree[idx * 2 + 1]
        )

    def query(self, idx, l, r, ql, qr):
        # Completely outside
        if r < ql or l > qr:
            return None

        # Completely inside
        if ql <= l and r <= qr:
            return self.tree[idx]

        mid = (l + r) // 2

        left = self.query(idx * 2, l, mid, ql, qr)
        right = self.query(idx * 2 + 1, mid + 1, r, ql, qr)

        if left is None:
            return right

        if right is None:
            return left

        # IMPORTANT: left must be merged before right
        return self.merge(left, right)


class Solution:
    def resultArray(
        self,
        nums: List[int],
        k: int,
        queries: List[List[int]]
    ) -> List[int]:

        n = len(nums)

        seg = SegmentTree(nums, k)

        ans = []

        for index, value, start, x in queries:

            # Persistent update
            seg.update(
                1,
                0,
                n - 1,
                index,
                value
            )

            # Query nums[start ... n-1]
            node = seg.query(
                1,
                0,
                n - 1,
                start,
                n - 1
            )

            ans.append(node.cnt[x])

        return ans