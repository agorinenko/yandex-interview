import collections
from typing import List


def test_1():
    arr = [6, 2, 3, 7, 0, 1]
    k = 3

    assert Solution().maxSlidingWindow(arr, k) == [6, 7, 7, 7]


def test_2():
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    assert Solution().maxSlidingWindow(arr, k) == [3, 3, 5, 5, 6, 7]


def test_3():
    arr = [1, -1]
    k = 1

    assert Solution().maxSlidingWindow(arr, k) == [1, -1]


def test_4():
    arr = [6, 2, 3, 7, 0, 1]
    k = 2

    assert Solution().maxSlidingWindow(arr, k) == [6, 3, 7, 7, 1]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # Используем монотонную двустороннюю очередь, максимум всегда будет в голове
        mono_deque = collections.deque()
        res = []
        for idx, num in enumerate(nums):
            while mono_deque and mono_deque[-1][0] <= num:
                mono_deque.pop()
            # Для каждого элемента добавляем в очередь его значение
            mono_deque.append((num, idx))

            # Удаляем левый элемент, если он за пределами окна
            if mono_deque[0][1] == idx - k:
                mono_deque.popleft()

            # Окно начнет двигаться - текущий индекс стал больше или равен k - 1
            if idx >= k - 1:
                # Добавляем максимум окна в результат
                res.append(mono_deque[0][0])
        return res

    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        """
        Time Complexity: O(n log(k)) since we have to push k elements into the heap and pop k elements out of the heap for each window.
        Space Complexity: O(n) for the heap
        """
        # Используем кучу максимумов, которая хранит k элементов
        max_heap, res = [], []
        for idx, num in enumerate(nums):
            # Для каждого элемента добавляем в кучу его значение и индекс
            heapq.heappush(max_heap, (-num, idx))
            # Окно начнет двигаться - текущий индекс стал больше или равен k - 1
            if idx >= k - 1:
                # В куче помимо числа мы также храним его индекс.
                # Сравниваем индекс максимального числа, и если оно уже не в окне - удаляем его
                while max_heap[0][1] <= idx - k:
                    heapq.heappop(max_heap)
                # Добавляем максимум окна в результат
                res.append(-max_heap[0][0])
        return res
