class Solution:
    def reverse(self, x: int) -> int:
        k=""
        sign = -1 if x < 0 else 1
        while(1):
            x=abs(x)
            m=x%10
            k=k+str(m)
            x=x//10
            if x==0 :
                break
        final_value = int(k)*sign
        if final_value< -2**31 or final_value > 2**31-1:
            return 0
        else:
            return final_value  
