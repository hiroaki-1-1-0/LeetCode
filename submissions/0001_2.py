class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            dif = target - num
            if dif in hash_map:
                return [i, hash_map[dif]]
            hash_map[num] = i