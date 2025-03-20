def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Time complexity : O(log(n))
        Space complexity : O(1)
        """
        left, right = 1, n
        while left <= right:
            num = (left + right) // 2
            result = guess(num)

            if result == 0:
                return num

            if result == 1:
                left = num + 1
            else:
                right = num - 1

        return -1
