class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count={}
        for element in nums:
            if element in count:
                count[element]+=1
            else:
                count[element]=1
        for key, value in count.items():
            if value == 1:
                return key
        return 1

        