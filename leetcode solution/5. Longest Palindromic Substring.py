class Solution:
    def longestPalindrome(self, s: str) -> str:
        output= ""
        for i in range(len(s)):
            left , right= i,i 
            while left>=0 and right < len(s) and s[right]==s[left]:
                left-=1
                right+=1
            p=s[left+1:right]  
            left , right= i,i+1 
            while left>=0 and right < len(s) and s[right]==s[left]:
                left-=1
                right+=1
            p2=s[left+1:right]   
            if len(p)>len(output):
                output=p
             
            if len(p2)>len(output):
                output=p2
        return output
        