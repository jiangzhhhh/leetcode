# 穷举
class Solution1:
    def mySqrt(self, x: int) -> int:
        i = 1
        k = 0
        while i <= x:
            if i * i <= x:
                k = i
            i += 1
        return k


# 二分查找
class Solution2:
    def mySqrt(self, x: int) -> int:
        l, r, k = 0, x, 0
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid > x:
                r = mid - 1
            else:
                k = mid
                l = mid + 1
        return k


# 牛顿迭代
class Solution3:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        # y=sqrt(x)
        # 反函数g(x)=x^2
        # solve g(x)-C = 0 for x
        # g(x)-C的导数k=g'(x)=2x
        # -------------------
        # 直线方程y=kx+b
        # 代入(x0,y0)=(x0,g(x0)-C)=(x0,x0^2-C),k=g'(x)=2x0
        # solve x0^2 - C = 2x0^2 + b for b
        # x0^2 - C = b + 2x0^2
        # b + 2x0^2 = x0^2 - C
        # b = x0^2 - C - 2x0^2
        # b = x0^2 - 2x0^2 - C
        # b = -x0^2 - C
        # -------------------
        # solve kx + b = 0 for x
        # x = -b/k
        C = x
        x0 = C
        while True:
            b0 = -x0**2 - C
            k0 = 2*x0
            x1 = -b0/k0
            if abs(x1-x0) < 0.0001:
                break
            x0 = x1
        return int(x0)


test = [9, 4, 8, 1, 2, 0]
solutions = [Solution1(), Solution2(), Solution3()]
for solution in solutions:
    result = []
    for t in test:
        result.append(solution.mySqrt(t))
    print(result)
# s = Solution3()
# print(s.mySqrt(9))
