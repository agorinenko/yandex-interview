from typing import List


def test_1():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert 1 == Solution().numIslands(grid)


def test_2():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert 3 == Solution().numIslands(grid)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Time Complexity: O(N*M)
        Space Complexity: O(1)
        """
        count = 0
        # Заходим в каждую ячейку матрицы
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Возможные варианты значений:
                # -1 суша обследована ранее
                # 0 вода
                # 1 суша нового острова
                if grid[i][j] == '1':
                    # нашли новый остров, рекурсивно обследуем его
                    dfs(grid, i, j)
                    # остров найден
                    count += 1
        return count


def dfs(grid: List[List[str]], i, j):
    # Вышли за пределы поля
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return

    # Если ячейку уже посещали или это вода, то прекращаем обследование
    if grid[i][j] == '-1' or grid[i][j] == '0':
        return

    # ставим пометку об обследовании, если это суша
    grid[i][j] = '-1'

    # Обследуем соседние ячейки
    dfs(grid, i - 1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)
