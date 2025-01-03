class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        tmp = -1

        if nums1 > nums2:
            nums1, nums2 = nums2, nums1

        for num1 in nums1:
            for i in range(tmp+1, len(nums2)):
                if num1 == nums2[i]:
                    ans.append(num1)
                    tmp = i
                    break

        return ans