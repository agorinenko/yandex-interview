from typing import List


def test_1():
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

def test_2():
    assert Solution().maxArea([1, 1]) == 1


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1

        max_amount = 0
        # Идем с лева на право и с права на лево
        while left_ptr < right_ptr:
            # Ищем площадь, min потому что вода выливается через наименьшую стенку
            amount = min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr)
            # Если она больше текущей, то устанавливаем ее в качестве текущей
            if amount > max_amount:
                max_amount = amount

            # Двигаем указатель в зависимости от того, какая стенка наименьшая.
            # Левый, если левая, в противном случае правый.
            # Задача - максимизировать площадь.
            if height[left_ptr] <= height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1

        return max_amount
