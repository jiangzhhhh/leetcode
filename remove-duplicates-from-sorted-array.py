from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        pos = 0
        i = 0
        while i < length:
            last = nums[pos]
            num = nums[i]
            if last != num:
                nums[pos+1] = num
                pos = pos + 1
            i += 1
        return pos+1


s = Solution()
# print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(s.removeDuplicates([]))
