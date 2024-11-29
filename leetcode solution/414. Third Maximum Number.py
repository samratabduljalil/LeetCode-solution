class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        Max1=float('-inf')
        Max2=float('-inf')
        Max3=float('-inf')
        for i in (nums):
            if i>Max1:
                Max1=i
        for i in (nums):
            if i>Max2 and i!=Max1 :
                Max2=i
        for i in (nums):
            if i>Max3 and i!=Max1 and i!=Max2:
                Max3=i
        if Max3 !=float('-inf'):
            return Max3
        return Max1    