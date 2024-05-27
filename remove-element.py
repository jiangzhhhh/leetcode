from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        if length == 0:
            return 0
        i = 0
        j = 0
        while i < length:
            while j < length:
                if nums[j] != val:
                    break
                j += 1
            if j >= length:
                break
            nums[i] = nums[j]
            j += 1
            i += 1
        return i


s = Solution()
s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
