class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        chckr = {}

        for i in nums:
            if i not in chckr:
                chckr[i] = 1
            else:
                chckr[i] += 1
        
        if max(chckr.values()) > 1:
            return True
        else:
            return False