class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, k = 0, x, 0
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                k = mid
                l = mid + 1
            else:
                r = mid - 1
        return k


s = Solution()
print(s.mySqrt(9))
print(s.mySqrt(4))
print(s.mySqrt(8))
print(s.mySqrt(1))
print(s.mySqrt(2))
