from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        if len_nums >= 2:
            for i in range(0, len_nums-1):
                for j in range(i+1, len_nums):
                    a = nums[i]
                    b = nums[j]
                    if b == target - a:
                        return [i, j]
        return []


s = Solution()
# print(s.twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(s.twoSum([3, 2, 4], 6))  # [1, 2]
