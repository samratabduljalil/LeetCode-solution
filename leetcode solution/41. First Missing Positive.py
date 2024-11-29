class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        Max = float('inf')
        flagOne=0
        mySet=set()    
        for i in nums:
            mySet.add(i)
        for i in nums:
            if Max<i:
                Max=i    
        for i in range(1,len(nums)+1):
            if i not in mySet:
                return i
        return len(nums)+1      