class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0] >= 'A' and word[0] <='Z':
            flag=1 
            flag2 = 0
            for i in range(1,len(word)):
                print(i)
                if word[i] >= 'A' and word[i] <='Z':
                    flag+=1
                elif word[i] >= 'a' and word[i] <='z':
                    flag2+=1
            if (flag == len(word)) or (flag2 == len(word)-1) :
                    return True
            else:
                    return False    
        else:
            for i in range(1,len(word)):
                if word[i] >= 'A' and word[i] <='Z':
                    return False
            return True

        