class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        Max=0
        count=0
        for i in nums:
            if i==1:
                count+=1
                if Max <=count :
                    Max=count
            else:
                count=0
        return Max        
        