class Solution:
    def convertToBase7(self, num: int) -> str:
        negative = num < 0
        num = abs(num)
        results = []
        while True:
            repeat = num // 7
            reminder = num % 7
            results.append(str(reminder))
            num = repeat
            if repeat == 0:
                break
        results.reverse()
        return ('-' if negative else '') + ''.join(results)


s = Solution()
print(s.convertToBase7(100))  # 202