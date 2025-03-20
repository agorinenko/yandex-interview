from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Time complexity : O(log(n))
        Space complexity : O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1
