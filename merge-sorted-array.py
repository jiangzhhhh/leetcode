from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = []
        for i in range(m):
            temp.append(nums1[i])

        i = 0
        j = 0
        k = 0
        while k < m+n:
            n1 = temp[i] if i < m else None
            n2 = nums2[j] if j < n else None
            if n1 is not None and n2 is not None:
                if n1 < n2:
                    nums1[k] = n1
                    i += 1
                else:
                    nums1[k] = n2
                    j += 1
            elif n1 is not None:
                nums1[k] = n1
                i += 1
            elif n2 is not None:
                nums1[k] = n2
                j += 1
            k += 1
        print(nums1)


s = Solution()
# s.merge([1, 2, 3, 0, 0, 0],  3, [2, 5, 6], 3)
# s.merge([1], 1, [], 0)
# s.merge([0], 0, [1], 1)
# s.merge([2, 0], 1, [1], 1)
# s.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
# s.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
s.merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3)  # [-1,0,0,1,2,2,3,3,3]
