class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        Max_lenth_num=0
        Min_lenth_num=0
        Digit_after_addition=[]
        On_Hand=0
        if len(num1)>len(num2):
            Max_lenth_num=num1
            Min_lenth_num=num2
        else:
            Max_lenth_num=num2
            Min_lenth_num=num1
        for i in range(len(Min_lenth_num)):
            digit1 = ord(Min_lenth_num[len(Min_lenth_num)-1-i])-ord('0')
            digit2 = ord(Max_lenth_num[len(Max_lenth_num)-1-i])-ord('0')
            result=digit1+digit2+On_Hand
            On_Hand=0
            if result <10:
                Digit_after_addition.append(result)
                On_Hand=0
            else:
                retrive_digit=result%10
                Digit_after_addition.append(retrive_digit)
                On_Hand=1
        for i in range(len(Min_lenth_num),len(Max_lenth_num)):
            digit1 = ord(Max_lenth_num[len(Max_lenth_num)-1-i])-ord('0')
            if On_Hand==1:
                result=digit1+On_Hand
                if result <10:
                    Digit_after_addition.append(result)
                    On_Hand=0
                else:
                    retrive_digit=result%10
                    Digit_after_addition.append(retrive_digit)
                    On_Hand=1                    
            else:
                result=digit1+On_Hand
                if result <10:
                   Digit_after_addition.append(result)
                   On_Hand=0
                else:
                    retrive_digit=result%10
                    Digit_after_addition.append(retrive_digit)
                    On_Hand=1
        if On_Hand==1:
            Digit_after_addition.append(1)            
        Reverse_digit_after_addition=list(reversed(Digit_after_addition))
        Added_string=""
        for char in Reverse_digit_after_addition:
            Added_string=Added_string+chr(char + ord('0'))
        return Added_string