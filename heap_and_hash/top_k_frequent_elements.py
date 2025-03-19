import collections
import heapq
from typing import List


def test_1():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    assert Solution().topKFrequent(nums, k) == [1, 2]


def test_2():
    nums = [4, 1, -1, 2, -1, 2, 3]
    k = 2
    assert Solution().topKFrequent(nums, k) == [-1, 2]


class Solution:
    def topKFrequent(self, nums, k):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        bucket = [[] for _ in range(len(nums) + 1)] #  + 0 index
        num_map = collections.defaultdict(int)
        for num in nums:
            num_map[num] += 1

        for num, freq in num_map.items():
            bucket[freq].append(num)

        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[::-1][:k]


    def topKFrequent_HEAP(self, nums: List[int], k: int) -> List[int]:
        """
        Time Complexity: O(n*log(K)) -> для каждого элемента O(n) вставить в кучу O(log(K))
        Space Complexity: O(n) -> O(n) для num_map и O(K) для кучи.
        """
        num_map = collections.defaultdict(int)
        for num in nums:
            num_map[num] += 1

        sorted_nums = []  # sorted(num_map.items(), key=lambda x: x[1], reverse=True)
        for num, count in num_map.items():
            heapq.heappush(sorted_nums, (-count, num))

        res = []
        for _ in range(k):
            item = heapq.heappop(sorted_nums)
            res.append(item[1])
        return res
