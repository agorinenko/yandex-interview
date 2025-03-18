import collections
from typing import List


def test_1():
    assert Solution().removeInvalidParentheses("()())()") == ["(())()","()()()"]

def test_2():
    assert Solution().removeInvalidParentheses("(a)())()") == ["(a())()", "(a)()()"]


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Используем очередь и поиск в ширину для набора всех возможных вариантов
        queue = collections.deque()
        # Добавляем входящую строку в конец
        queue.append(s)
        # Заводим набор просмотренных строк, чтобы не обрабатывать одно и тоже несколько раз
        visited = set()
        result = []
        stop_traverse = False
        while queue:
            # Берем строку из головы
            item = queue.popleft()
            # если ее уже обрабатывали, то пропускаем
            if item in visited:
                continue
            # добавляем в просмотренные
            visited.add(item)
            # если строка имеет правильную скобочную последовательность, то добавляем к результату и прекращаем обработку ее подстрок
            if is_valid(item):
                # Останавливаем обработку текущего элемента, тк любое удаление скобки приведет к неправильной последовательности
                stop_traverse = True
                result.append(item)

            if not stop_traverse:
                # для всех символов текущей строки
                for i in range(len(item)):
                    if item[i] in {'(', ')'}:
                        # добавляем в очередь варианты текущей строки без скобки
                        queue.append(f'{item[:i]}{item[i + 1:]}')

        return result


def is_valid(s: str) -> bool:
    stack = []

    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return False

            stack.pop()

    return len(stack) == 0