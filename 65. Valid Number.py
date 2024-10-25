class Solution:
    def isNumber(self, s: str) -> bool:
        flag=0
        flagmp=0
        flagnum=0
        count_e = 0
        count_d =0
        count_c=0
        for i in range(0,len(s)):
            if s[i]>='0' and s[i]<='9':
                flagnum=1
                if(flag==1):
                    flag=0
            elif (s[i]>='A' and s[i]<='Z') or (s[i]>='a' and s[i]<='z') :
                if s[i]>='e' or s[i]<='E':
                    if flagnum==1 and count_e==0:
                        
                        flag=1
                        count_e +=1
                        print(count_e)
                    else :
                        return False
                    
            elif s[i]=='+' or s[i]=='-':
                
                if (flag==1 or flagnum==1) and flagmp<=2:
                    flag=0
                elif flagmp==0:
                       flagmap=1
                else:
                    return False

            
               
                flagmp=+1
            elif s[i]=='.':
                
                
                if count_d ==0 and flagnum==1 and count_e==0 :
                    cout_d =+1
                else:
                    return False
        if flag==0:
            return True 
        else :
            return False         