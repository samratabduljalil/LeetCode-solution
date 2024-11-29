class Solution:
    def myAtoi(self, s: str) -> int:
        flag=0
        flagc=0
        flagmp=0
        out=""
        for i in range(0,len(s)):  
            if (s[i]=='0' and flag==1):
                out=out+s[i]
                print(out)
            elif((s[i]=='-' or s[i]=='+')):
                if flag ==0:
                    if flagmp==0:
                        out=out+s[i]
                        flagmp=1 
                    else :
                        flagmp=1 
                        break   
                else:
                    break      
            elif(s[i]>='1' and s[i]<='9'):
                out=out+s[i]  
                flag=1  
            elif((s[i]>='A' and s[i]<='Z') or (s[i]>='a' and s[i]<='z')or s[i]=='.' ):
                break 
            elif s[i]=='0':
                flagmp=1
            elif((flagmp==1 or flag==1) and s[i]==' '):
                break
        if flag==0:
            out=out+'0'
        INT32_MIN=-2**31
        INT32_MAX=2**31-1     
        output=int(out)
        if output < INT32_MIN:
            output = INT32_MIN
        elif output > INT32_MAX:
            output = INT32_MAX       
        return output

        