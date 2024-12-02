class Solution(object):
    def twoSum(self, nums, target):
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num_i in enumerate(nums):
            for j, num_j in enumerate(nums[i+1:]):
                if target == num_i + num_j:
                    return [i, j + i + 1]