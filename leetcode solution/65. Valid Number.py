class Solution:
    def isNumber(self, s: str) -> bool:
        flag=0
        flagmp=0
        flagnum=0
        count_e = 0
        count_d =0
        count_c=0
        flagd=0
        for i in range(0,len(s)):
            if s[i]>='0' and s[i]<='9':
                flagnum=1
                if(flag==1):
                    flag=0
            elif (s[i]>='A' and s[i]<='Z') or (s[i]>='a' and s[i]<='z') :
                if s[i]=='e' or s[i]=='E':
                    if flagnum==1 and count_e==0:
                        flag=1
                        count_e +=1
                    else :
                        return False
                else:
                    return False    
            elif s[i]=='+' or s[i]=='-':
                if flagd==1:
                   return False
                if count_d>1:
                    return False   
                elif (flag==1 and flagnum==1) and flagmp<=2:
                    flag=1   
                elif flagnum==1 :
                    return False
                elif flagmp==0:
                       flagmap=1
                else:
                    return False  
                flagmp=+1
                flag=1
            elif s[i]=='.':
                flagd=1
                if flagnum==0:
                    flag=1
                if count_d ==0 and  count_e==0 :
                    count_d +=1
                    continue
                else:
                    return False
                count_d +=1
                continue
            flagd=0
        print(flag)
        if flag==0 and (count_d!=len(s)):
            return True 
        else :
            return False           



                

        