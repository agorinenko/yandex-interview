from typing import List


def test_1():
    assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]


def test_2():
    assert Solution().partitionLabels("eccbbbbdec") == [10]


def test_3():
    assert Solution().partitionLabels("qiejxqfnqceocmy") == [13, 1, 1]


class Solution:
    """ Символы не присутствуют за пределами своего раздела """

    def partitionLabels(self, s: str) -> List[int]:
        """
        Time Complexity: O(N), where N is the length of S.
        Space Complexity: O(1) to keep data structure last of not more
        than 26 characters.
        """
        last_idx = {}  # Словарь символ -> последняя позиция символа в строке
        for i, c in enumerate(s):
            last_idx[c] = i

        res = []
        # текущий размер группы и указатель на возможный конец группы
        size, end = 0, 0
        for i, c in enumerate(s):
            # Увеличиваем размер группы
            size += 1
            # Рассчитываем указатель на возможный конец группы на основе текущего элемента
            # end может сдвинуться вправо, если последнее вхождение текущего символа в строке больше чем end
            end = max(end, last_idx[c])
            # Если текущая позиция достигла конца группы
            if end == i:
                # Добавляем размер группы в ответ и затем обнуляем его
                # end не обнуляем, на следующей итерации списка он передвинется вправо
                res.append(size)
                size = 0

        return res
