class Solution(object):
    def countSmaller(self, nums):
        n = len(nums)

        # Stores the answer
        count = [0] * n

        # Store (value, original_index)
        arr = [(nums[i], i) for i in range(n)]

        def merge_sort(left, right):
            if left >= right:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid + 1, right)

            merge(left, mid, right)

        def merge(left, mid, right):
            temp = []

            i = left          # Left half pointer
            j = mid + 1       # Right half pointer

            rightCount = 0

            while i <= mid and j <= right:

                # Right element is smaller
                if arr[j][0] < arr[i][0]:
                    temp.append(arr[j])
                    rightCount += 1
                    j += 1

                else:
                    # All previously moved right elements
                    # are smaller than arr[i]
                    count[arr[i][1]] += rightCount
                    temp.append(arr[i])
                    i += 1

            # Remaining left elements
            while i <= mid:
                count[arr[i][1]] += rightCount
                temp.append(arr[i])
                i += 1

            # Remaining right elements
            while j <= right:
                temp.append(arr[j])
                j += 1

            # Copy back
            for k in range(len(temp)):
                arr[left + k] = temp[k]

        merge_sort(0, n - 1)

        return count