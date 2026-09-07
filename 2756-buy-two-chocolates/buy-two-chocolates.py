class Solution(object):
    def buyChoco(self, prices, money):
        prices.sort()

        total = prices[0] + prices[1]

        if total <= money:
            return money - total
        else:
            return money