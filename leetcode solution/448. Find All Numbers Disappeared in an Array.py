class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums2=set(nums)
        n2=len(nums2)
        list_dis=[]
        for i in range(1,len(nums)+1):
            list_dis.append(i)
        nums3=set(list_dis)
        return list(nums2.symmetric_difference(nums3))
        