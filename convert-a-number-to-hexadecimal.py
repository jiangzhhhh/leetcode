class Solution:
    def toHex(self, num: int) -> str:
        alphabet = '0123456789abcdef'
        results = []
        if num < 0:
            num = 2**32 + num
        while True:
            repeat = num // 16
            reminder = num % 16
            results.append(alphabet[reminder])
            num = repeat
            if repeat == 0:
                break
        results.reverse()
        return ''.join(results)

s = Solution()
# print(s.toHex(26))  # "1a"
print(s.toHex(-1))  # "ffffffff"
# print(s.toHex(0))  # "0"
# print(s.toHex(16))  # "10"
# print(s.toHex(17))  # "11"
# print(s.toHex(1700))  # "6a4"