class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        catch_first_str=strs[0]
        temp_str=''
        for i in range(1,len(strs)):
            flag=0
            for j in range(min(len(catch_first_str), len(strs[i]))):
                if catch_first_str[j]==strs[i][j]:
                    if flag==j: 
                        flag+=1
                        temp_str=temp_str+catch_first_str[j]
                    else:
                        break 
            catch_first_str=temp_str
            temp_str=''
        return catch_first_str


        