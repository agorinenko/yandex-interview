import collections
from typing import List


def test_1():
    s = "cbaebabacd"
    p = "abc"
    assert Solution().findAnagrams(s, p) == [0, 6]


def test_2():
    s = "baa"
    p = "aa"
    assert Solution().findAnagrams(s, p) == [1]


def encode_string(s: str) -> collections.defaultdict:
    """
    Преобразуем строку в хеш-таблицу с количеством повторений символов char->count
    """
    res = collections.defaultdict(int)

    for c in s:
        res[c] += 1

    return res


def is_anagram(window_code: dict, p_code: dict) -> bool:
    """
    Проверка, что закодированные строки являются анаграммами.
    Т.е количество повторений для каждого символа в таблицах равны.
    """
    for char, count in window_code.items():
        if count > 0 and (char not in p_code or p_code[char] != count):
            return False

    return True


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        l, r = 0, len(p)
        # Кодируем входящую строку р
        p_code = encode_string(p)
        # Кодируем окно, равное длине входящей строки р
        window_code = encode_string(s[l:r])

        res = []
        # Пока правый край окна не достигнет конца строки S
        while r < len(s):
            # Проверяем на анаграмму
            if is_anagram(window_code, p_code):
                res.append(l)
            # Удаляем левый символ из кодированного представления окна
            left_char = s[l]
            window_code[left_char] -= 1
            # Добавляем правый символ к кодированному представления окна(изначально символ с индексом r не включен в окно)
            right_char = s[r]
            window_code[right_char] += 1
            # Двигаем окно слева на право
            l += 1
            r += 1
        # Т.к изначально символ с индексом r не включен в окно, нам надо проверить кодированные представления после цикла
        if is_anagram(window_code, p_code):
            res.append(l)

        return res
