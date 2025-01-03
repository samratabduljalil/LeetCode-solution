class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []
        carry = 0
        i = len(num) - 1
        
        while i >= 0 or k > 0:
            X = num[i] if i >= 0 else 0
            Y = k % 10
            
            total = X + Y + carry
            result.append(total % 10)
            carry = total // 10
            
            i -= 1
            k //= 10
        
        # Handle any remaining carry
        if carry:
            result.append(carry)
        
        # Reverse the result to get the final array form
        return result[::-1]
 

        