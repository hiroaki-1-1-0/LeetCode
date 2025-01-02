class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        chckr = {}
        
        for num in nums:
            chckr[num] = chckr.get(num, 0) + 1
            
        if max(chckr.values()) > 1:
            return True
        else:
            return False