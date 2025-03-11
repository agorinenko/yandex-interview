from typing import List


def test_1():
    nums = [-4, -1, 0, 3, 10]
    assert Solution().sortedSquares(nums) == [0, 1, 9, 16, 100]


def test_2():
    nums = [-7, -3, 2, 3, 11]
    assert Solution().sortedSquares(nums) == [4, 9, 9, 49, 121]


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Time Complexity: O(N) проходим по всем элементам массива
        Space Complexity: O(N) для хранения нового массива
        """
        res = []
        l, r = 0, len(nums) - 1
        # проходим по всем элементам массива 2-я указателями слева и справа навстречу друг другу, пока указатели не сойдутся
        while l <= r:
            # Вычисляем квадрат чисел на которые указывают указатели и сравниваем их.
            # Большее(тк исходный массив возрастает) значение добавляем к результату.
            if nums[l] * nums[l] > nums[r] * nums[r]:
                res.append(nums[l] * nums[l])
                l += 1
            else:
                res.append(nums[r] * nums[r])
                r -= 1
        # Получаем убывающий массив([121, 49, 9, 9, 4]), а нужен возрастающий, поэтому делаем разворот списка
        return res[::-1]
