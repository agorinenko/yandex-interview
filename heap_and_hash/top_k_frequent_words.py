import collections
from typing import List


def test_1():
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    assert Solution().topKFrequent(words, k) == ["i", "love"]


def test_2():
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    assert Solution().topKFrequent(words, k) == ["the", "is", "sunny", "day"]


def build_counter(words: List[str]) -> dict:
    data = collections.defaultdict(int)
    for word in words:
        data[word] += 1
    return data


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Time Complexity: O(n*log(n)) for sorted
        Space Complexity: O(n) to keep counter.
        """
        counter = build_counter(words)
        sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]), reverse=False)
        return [i[0] for i in sorted_counter[:k]]
