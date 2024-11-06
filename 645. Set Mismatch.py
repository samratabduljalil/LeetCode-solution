class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        original_Sum=n*(n+1)//2
        Sum_of_all_nums=sum(nums)
        Sum_without_duplicate=sum(set(nums))
        return[Sum_of_all_nums-Sum_without_duplicate,original_Sum-Sum_without_duplicate]
