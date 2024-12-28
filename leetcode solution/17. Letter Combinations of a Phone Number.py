class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_letter_combo={
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
         } 
        combo=list(digit_letter_combo[digits[0]])

        for i in range(1,len(digits)):
            current_letters = digit_letter_combo[digits[i]]
            new_combo=[]
            for letters in combo:
                for letter in current_letters:
                    new_combo.append(letters+letter)
            combo=new_combo
        return combo                  