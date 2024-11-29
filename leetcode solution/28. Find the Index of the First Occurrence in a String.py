class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        for i in range(0,len(haystack)):
            if (len(haystack)-i) < len(needle):
                return -1;
            if haystack[i]==needle[0]:
                flag=0;
                for j in range(0,len(needle)):
                     if haystack[i+j]==needle[j]:
                        flag +=1
                        print(flag)
                if flag == len(needle):
                        return i;
        return -1