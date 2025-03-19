from typing import List


def test_1():
    num = [1, 2, 0, 0]
    k = 34
    assert Solution().addToArrayForm(num, k) == [1, 2, 3, 4]


def test_2():
    num = [2, 7, 4]
    k = 181
    assert Solution().addToArrayForm(num, k) == [4, 5, 5]


def test_3():
    num = [2, 1, 5]
    k = 806
    assert Solution().addToArrayForm(num, k) == [1, 0, 2, 1]


def test_4():
    num = [2, 1, 5]
    k = 1806
    assert Solution().addToArrayForm(num, k) == [2, 0, 2, 1]


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        k_array = [int(c) for c in str(k)][::-1]
        num = num[::-1]

        res = []

        max_len = max(len(num), len(k_array))
        carry = 0
        for i in range(max_len):
            a = num[i] if i < len(num) else 0
            b = k_array[i] if i < len(k_array) else 0

            s = a + b + carry
            carry = s // 10
            tail = s % 10
            res.append(tail)

        if carry > 0:
            res.append(carry)

        return res[::-1]
