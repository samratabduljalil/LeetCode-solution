class Solution:
    def isPalindrome(self, x: int) -> bool:
        stri = str(x)
        
        text = "Hello, World!"
        reversed_text = stri[::-1]
        if reversed_text == stri:
            return True
        return False    

        