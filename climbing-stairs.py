from typing import List


# class Solution:
#     def climb(self, n: int) -> int:
#         count = 0
#         for s in [1, 2]:
#             remain = n - s
#             if remain > 0:
#                 count += self.climb(remain)
#             elif remain == 0:
#                 count += 1
#         return count

#     def climbStairs(self, n: int) -> int:
#         return self.climb(n)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        y0 = 1
        y1 = 2
        y2 = y0 + y1
        i = 3
        while i <= n:
            y2 = y0 + y1
            y0 = y1
            y1 = y2
            i += 1
        return y2


# 0,1,2,3,5
s = Solution()
print(s.climbStairs(0))
print(s.climbStairs(1))
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
print(s.climbStairs(5))
# print(s.climbStairs(38))
