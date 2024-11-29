class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Max= 0
        Min= float('inf') 
        for i in range(len(prices)):  
            if (prices[i]-Min)> Max:
                Max = (prices[i]-Min)
            elif prices[i]< Min:
                Min= prices[i]
        return Max            