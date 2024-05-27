def get_bit(s: str, i: int, max: int) -> int:
    size = len(s)
    if size < max:
        padding = max - size
        j = i - padding
        if j < 0:
            return 0
        else:
            return int(s[j])
    return int(s[i])


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_size = max(len(a), len(b))
        adv = 0
        result = []
        for i in range(max_size - 1, -1, -1):
            a_bit = get_bit(a, i, max_size)
            b_bit = get_bit(b, i, max_size)
            sum = a_bit + b_bit + adv
            c_bit = sum % 2
            adv = sum // 2
            # print(i, a_bit, b_bit, adv, c_bit)
            result.append(c_bit)
        if adv > 0:
            result.append(1)
        result.reverse()
        result = map(lambda x: str(x), result)
        return "".join(result)


s = Solution()
print(s.addBinary("11", "1"))
print(s.addBinary("1010", "1011"))
