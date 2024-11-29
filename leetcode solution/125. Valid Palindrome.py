       
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower=[]
        for i in s:
            if i>='A' and i<='Z':
                lower.append(chr(ord(i)+32))
            elif  i>='a' and i<='z':
                lower.append(i)
            elif  i>='0' and i<='9':
                lower.append(i)
        for i in range(len(lower)):
            if   lower[i]!=lower[len(lower)-1-i]:
                return False               
        return True  