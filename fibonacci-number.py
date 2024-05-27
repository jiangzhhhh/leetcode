class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        y0 = 0
        y1 = 1
        y2 = y0+y1
        i = 2
        while i <= n:
            y2 = y0 + y1
            y0 = y1
            y1 = y2
            i += 1
        return y2
