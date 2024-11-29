class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        high=len(nums)-1
        low=0
        flag=1
        mid=0
        while(low<=high):
            mid=(low+high+1)//2
            if nums[mid] == target:
                flag=0
                break
            elif target > nums[mid]:
                low=mid+1
            else:
                high=mid-1 
        if flag==1:
            return [-1,-1]
        start=mid 
        end=mid     
        while(start>=0):
            if nums[start]!=target:
                break
            if nums[start]==target:
                start -=1     
        while(end<=len(nums)-1):
            if nums[end]!=target:
                break
            if nums[end]==target:
                end +=1   
        return [start+1,end-1]       