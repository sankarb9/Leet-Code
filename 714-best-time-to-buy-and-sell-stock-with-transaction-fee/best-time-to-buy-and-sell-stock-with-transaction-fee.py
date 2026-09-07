class Solution(object):
    def maxProfit(self, prices, fee):
        hold=-prices[0]
        cash=0
        for i in range(1,len(prices)):
            cash=max(cash,hold+prices[i]-fee)
            hold=max(hold,cash-prices[i])
        return cash