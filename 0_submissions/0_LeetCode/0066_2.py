class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        
        for digit in reversed(digits):
            if digit != 9:
                digits[index] += 1
                return digits

            digits[index] = 0
            index -= 1
            
            if index == 0 and digits[index] == 9:
                digits[index] = 0
                return [1] + digits
                
        return [1,0]