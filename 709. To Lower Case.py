class Solution:
    def toLowerCase(self, s: str) -> str:
        for i in range(0,len(s)):
            if 'A' <= s[i] <= 'Z':
                s=s.replace(s[i],chr(ord(s[i])+32))
        return s