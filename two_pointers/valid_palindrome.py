class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        left_ptr = 0
        right_ptr = len(s) - 1

        while left_ptr < right_ptr:
            while not s[left_ptr].isalnum() and left_ptr < right_ptr:
                left_ptr += 1

            while not s[right_ptr].isalnum() and left_ptr < right_ptr:
                right_ptr -= 1

            if s[left_ptr].lower() != s[right_ptr].lower():
                return False

            left_ptr += 1
            right_ptr -= 1

        return True