from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N).
        Space Complexity: O(N).
        """
        data = set()
        for i in nums:
            if i in data:
                data.remove(i)
            else:
                data.add(i)

        return data.pop()