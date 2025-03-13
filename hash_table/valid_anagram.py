import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = collections.defaultdict(int)
        t_map = collections.defaultdict(int)

        for i in range(len(s)):
            s_map[s[i]] += 1
            t_map[t[i]] += 1

        for k, v in s_map.items():
            if v != t_map[k]:
                return False

        return True