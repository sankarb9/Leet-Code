class Solution(object):
    def minimumBoxes(self, apple, capacity):
        total_apples = sum(apple)

        capacity.sort(reverse=True)

        current_capacity = 0
        boxes = 0

        for cap in capacity:
            current_capacity += cap
            boxes += 1

            if current_capacity >= total_apples:
                return boxes