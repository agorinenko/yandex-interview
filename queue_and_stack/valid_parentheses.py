class Solution:
    def isValid(self, s: str) -> bool:
        opened_chars = {'(', '{', '['}
        map_chars = {
            '(': ')', '{': '}', '[': ']'
        }
        stack = []
        for char in s:
            if char in opened_chars:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                stack_char = stack.pop()
                if char != map_chars[stack_char]:
                    return False

        return len(stack) == 0