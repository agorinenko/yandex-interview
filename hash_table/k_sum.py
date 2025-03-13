from typing import List


def test_1():
    """ Трейс вызовов
    -----------
    nums: [-2, -1, 0, 0, 1, 2], target: 0, k: 4
    -----------
    nums: [-1, 0, 0, 1, 2], target: 2, k: 3
    -----------
    nums: [0, 0, 1, 2], target: 3, k: 2
    -----------
    nums: [0, 1, 2], target: 2, k: 2
    -----------
    nums: [2], target: 1, k: 2
    -----------
    nums: [], target: 0, k: 2
    -----------
    nums: [0, 0, 1, 2], target: 1, k: 3
    -----------
    nums: [0, 1, 2], target: 1, k: 2
    -----------
    nums: [2], target: 0, k: 2
    -----------
    nums: [], target: -1, k: 2
    -----------
    nums: [0, 1, 2], target: 0, k: 3
    -----------
    nums: [1, 2], target: 0, k: 2
    -----------
    nums: [2], target: -1, k: 2
    -----------
    nums: [], target: -2, k: 2
    -----------
    nums: [2], target: -1, k: 3
    -----------
    nums: [], target: -3, k: 2
    -----------
    nums: [], target: -2, k: 3

    """
    nums = [1, 0, -1, 0, -2, 2]
    target = 0

    assert Solution().fourSum(nums, target) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]


def test_2():
    """
    Трейс вызовов
    -----------
    nums: [2, 2, 2, 2, 2], target: 8, k: 4
    -----------
    nums: [2, 2, 2, 2], target: 6, k: 3
    -----------
    nums: [2, 2, 2], target: 4, k: 2
    """
    nums = [2, 2, 2, 2, 2]
    target = 8

    assert Solution().fourSum(nums, target) == [[2, 2, 2, 2]]


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Time Complexity: O(n^k−1), or O(n^3) for 4Sum. We have k−2 loops iterating over n elements, and twoSum is O(n).
        Space Complexity: O(n) for the hash set. The space needed for the recursion will not exceed O(n).
        """
        # Сортируем массив, чтобы пропустить дубликаты в дальнейшем n*log(n), но для k>2, сортировка не увеличит временную сложность
        nums.sort()
        # Вызываем универсальную функцию для k=4
        return k_sum(nums, target, 4)


def k_sum(nums: List[int], target: int, k: int) -> List[List[int]]:
    if not nums:
        return []
    # Базовый случай рекурсии для k=2
    if k == 2:
        return two_sum(nums, target)

    result = []

    for idx, num in enumerate(nums):
        # не обрабатываем повторяющиеся элементы, по условию quadruplets уникальны
        if idx == 0 or nums[idx - 1] != nums[idx]:
            # Для каждого элемента рекурсивно ищем наборы, которые
            # 1) находятся в массиве, следующем после этого элемента
            # 2) значение target суммы набора равно target - этот элемент
            # 3) количество элементов в наборе к, меньше текущего количества на 1

            subsets = k_sum(nums[idx + 1:], target - num, k - 1)
            # если для текущего элемента нашлись наборы, то добавляем их к результату текущего вызова
            for subset in subsets:
                result.append([num] + subset)
    return result


def two_sum(nums: List[int], target: int) -> List[List[int]]:
    result = []
    s = set()
    for idx, num in enumerate(nums):
        diff = target - num
        # по условию quadruplets уникальны, если предыдущая запись result уже содержит такой результат, то не добавляем
        if not result or num != result[-1][1]:
            if diff in s:
                result.append([diff, num])

        s.add(num)

    return result
