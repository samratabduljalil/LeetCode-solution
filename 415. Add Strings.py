class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n=0
        s=0
        k=[]
        m=0
        if len(num1)>len(num2):
            n=num1
            s=num2
        else:
            n=num2
            s=num1

        for i in range(len(s)):
            digit1 = ord(s[len(s)-1-i])-ord('0')
            digit2 = ord(n[len(n)-1-i])-ord('0')
            result=digit1+digit2+m
            m=0
            if result <10:
                k.append(result)
                m=0
            else:
                l=result%10
                k.append(l)
                m=1
        for i in range(len(s),len(n)):
            digit1 = ord(n[len(n)-1-i])-ord('0')
            if m==1:
                result=digit1+m
                if result <10:
                    k.append(result)
                    m=0
                else:
                    l=result%10
                    k.append(l)
                    m=1
                    
            else:
                result=digit1+m
                if result <10:
                   k.append(result)
                   m=0
                else:
                    l=result%10
                    k.append(l)
                    m=1
        if m==1:
            k.append(1)            
        ink=list(reversed(k))
        j=""
        for i in ink:
            j=j+chr(i + ord('0'))
        return j





            



        