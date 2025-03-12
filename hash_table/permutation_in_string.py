import collections


def test_1():
    s1 = "ab"
    s2 = "eidbaooo"
    assert Solution().checkInclusion(s1, s2)


def test_2():
    s1 = "ab"
    s2 = "eidboaoo"
    assert not Solution().checkInclusion(s1, s2)

def test_3():
    s1 = "ab"
    s2 = "a"
    assert not Solution().checkInclusion(s1, s2)


def encode_str(s: str) -> collections.defaultdict:
    enc = collections.defaultdict(int)
    for c in s:
        enc[c] += 1
    return enc


def is_inclusion(example: dict, target: dict) -> bool:
    for char, count in example.items():
        if count > 0:
            if char not in target or count != target[char]:
                return False

    return True


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Смотри пояснения в ./hash_table/find_all_anagrams_in_a_string.py
        """
        if len(s1) > len(s2):
            return False
        l, r = 0, len(s1)
        window_enc = encode_str(s2[l:r])
        target_enc = encode_str(s1)
        while r < len(s2):
            if is_inclusion(window_enc, target_enc):
                return True

            l_char = s2[l]
            r_char = s2[r]
            window_enc[l_char] -= 1
            window_enc[r_char] += 1
            l += 1
            r += 1

        if is_inclusion(window_enc, target_enc):
            return True

        return False
