class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            top = stack[-1] if stack else None
            if c in pairs and pairs[c] == top:
                # 当前输入跟栈顶元素匹配的话，就弹出栈顶元素
                stack.pop()
            else:
                # 否则入栈
                stack.append(c)
        # 如果栈为空，说明所有元素都匹配了
        return not stack


s = Solution()
