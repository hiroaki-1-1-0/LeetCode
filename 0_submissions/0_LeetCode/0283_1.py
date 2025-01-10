class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cntr = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                cntr+= 1
                
            else:
                nums[i-cntr] = nums[i]
        
        for i in range(len(nums)-1, len(nums)-cntr-1, -1):
            nums[i] = 0
        
        return nums