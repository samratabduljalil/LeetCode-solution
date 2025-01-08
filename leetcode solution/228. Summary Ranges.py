class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not  nums:
            return []
        List = []

        take = nums[0]
        for i in range(1,len(nums)):
         
            if nums[i] != nums[i-1]+1:
                if take == nums[i-1]:
                    List.append(f"{take}")
                else:
                    List.append(f"{take}->{nums[i-1]}") 
                take=nums[i]

        if take == nums[-1]:
            List.append(f"{take}")
        else:
            List.append(f"{take}->{nums[-1]}")

        return List                   



        