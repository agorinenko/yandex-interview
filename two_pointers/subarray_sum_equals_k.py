from typing import List


def test_1():
    nums = [1, 1, 1]
    k = 2
    assert Solution().subarraySum(nums, k) == 2


def test_2():
    nums = [1, 2, 3]
    k = 3
    assert Solution().subarraySum(nums, k) == 2


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Time complexity : O(n^2) - для каждого числа делаем второй проход
        Space complexity : O(n) - под cumulative сумму
        """
        count = 0
        # Рассчитываем cumulative сумму - массив длинной len(nums) + 1 чисел
        sums_map = [0]  # [0, 1, 3, 6] для [1, 2, 3]
        for i in range(1, len(nums) + 1):
            sums_map.append(sums_map[i - 1] + nums[i - 1])
        # Для каждого числа
        for l in range(len(nums)):
            # для каждого подмассива...
            for r in range(l + 1, len(nums) + 1):
                # sub_array = nums[l:r]
                # if sum(sub_array) == k:
                #     count += 1
                # вычисляем сумму всех элементов подмассива, основываясь на cumulative суммах
                if sums_map[r] - sums_map[l] == k:
                    count += 1

        return count
