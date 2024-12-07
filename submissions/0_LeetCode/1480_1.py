class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        tmp = 0
        for i, num in enumerate(nums):
            tmp += num
            ans.append(tmp)
        return ans