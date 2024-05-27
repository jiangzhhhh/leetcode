from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        i = 0
        while i < length:
            n = nums[i]
            if n >= target:
                return i
            i += 1
        return length


s = Solution()
# print(s.searchInsert([1, 3, 5, 6], 5))  # 2
# print(s.searchInsert([1, 3, 5, 6], 2))  # 1
print(s.searchInsert([1, 3, 5, 6], 7))  # 4
