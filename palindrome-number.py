class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = x
        arr = []
        while True:
            arr.append(y % 10)
            y = y // 10
            if y == 0:
                break
        len_arr = len(arr)
        mid = len_arr // 2
        for i in range(0, mid):
            # print(i, arr[i], arr[len_arr - i - 1])
            if arr[i] != arr[len_arr - i - 1]:
                return False
        return True


# print(Solution().isPalindrome(121))  # True
# print(Solution().isPalindrome(-121))  # False
# print(Solution().isPalindrome(123))  # False
print(Solution().isPalindrome(10))  # False
print(Solution().isPalindrome(11))  # True
