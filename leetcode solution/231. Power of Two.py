class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count=0
        while(1):
            if n== 2**count:
                return True
            elif  n< 2**count :
                return False
            count+=1        