import collections
from typing import List


def test_1():
    assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["bat"], ["nat", "tan"],
                                                                                    ["ate", "eat", "tea"]]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time Complexity: O(N), where N is the length of S.
        Space Complexity: O(1) to keep data structure last of not more than 26 characters.
        """
        results = collections.defaultdict(list)
        for s in strs:
            key = encode_str(s)
            results[key].append(s)
        return list(results.values())


def encode_str(s: str) -> str:
    encode_dict = collections.defaultdict(int)
    for c in s:
        encode_dict[c] += 1

    keys = sorted(encode_dict.keys())
    res = []
    for k in keys:
        res.append(f'{k}{encode_dict[k]}')

    return ''.join(res)
