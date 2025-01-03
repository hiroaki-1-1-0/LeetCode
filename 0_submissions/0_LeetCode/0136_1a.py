# "a" means "Try Again, Later"
# Python has bitwise operators for integers: & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        You must implement a solution with a linear runtime complexity and use only constant extra space.
        """
        ans = 0
        
        for num in nums:
            ans ^= num
        
        return ans