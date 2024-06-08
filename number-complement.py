class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 0
        i = 31
        leading = True
        result = 0
        while i >= 0:
            bit = (num >> i) & 0x1
            if leading and bit == 1:
                leading = False
            if not leading:
                neg = (~bit + 2)
                result |= (neg << i)
            i -= 1
        return result

s = Solution()
print(s.findComplement(5))  # 2