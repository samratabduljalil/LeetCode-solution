class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        X=[]
        Y=[]
        for i in range(n):
            X.append(nums[i])
        for i in range(n,len(nums)):
            Y.append(nums[i])  
        Xi=0
        Yi=0
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=X[Xi]  
                Xi+=1
            else:
                nums[i]=Y[Yi]  
                Yi+=1
        return nums       
