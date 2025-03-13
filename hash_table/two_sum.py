from typing import List, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Tuple[int, int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        data = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in data:
                return idx, data[diff]
            else:
                data[num] = idx

        return -1, -1