class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cntr = 0
        tmp = -1000

        for num in nums:
            if num != tmp:
                nums[cntr] = num
                cntr += 1
            tmp = num
        
        return cntr