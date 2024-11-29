class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        if k==0 or k==len(nums):
            return
        if k>len(nums):
            for i in range(k):
                temp=nums[0]
                nums[0]=nums[len(nums)-1]
                for j in range(1,len(nums)):
                    temp2=nums[j]
                    nums[j]=temp
                    temp=temp2
        else:
            for i in range(k-1,-1,-1):
                l.append(nums[len(nums)-1-i])
            for i in range(len(nums)-k):
                l.append(nums[i])
            for i in range(len(l)):
                nums[i]=l[i]

        