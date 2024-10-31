class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums = {}
        for element in nums2:
            if element in nums:
                nums[element] += 1  
            else:
                nums[element] = 1
        for element in nums1:
            if element in nums:
                if(nums[element]>=1):
                    nums[element] -= 1 
                    intersection.append(element)     
        return intersection