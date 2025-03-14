import collections


def test_1():
    s = "ABAB"
    k = 2
    assert Solution().characterReplacement(s, k) == 4

def test_2():
    s = "AABABBA"
    k = 1
    assert Solution().characterReplacement(s, k) == 4


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, res = 0, 0

        stats = collections.defaultdict(int)
        for right, char in enumerate(s):
            stats[char] += 1
            # Двигаем левый указатель пок длина окна минус максимальное кол-во символов одного типа в окне больше K количества перестановок
            while (right - left + 1) - max(stats.values()) > k:
                stats[s[left]] -= 1
                left += 1
            # На данном этапе максимальное значение непрерывной последовательности одних символов равно большему из длины окна и предыдущему кандидату на ответ
            res = max(res, (right - left + 1))

        return res
