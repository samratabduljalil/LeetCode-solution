class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        for i in range(len(s) - 1, -1, -1):
            if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
                for j in range(i, -1, -1):
                    if s[j] == " ":
                        return i-j
                    elif j == 0:
                        return i-j+1