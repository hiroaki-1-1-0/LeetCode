class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans_nums = nums
        for i in range(1, len(nums)):
            ans_nums[i] += nums[i-1]
        return ans_nums