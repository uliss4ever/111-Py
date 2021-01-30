from typing import List



def merge(left, right):
    ssorted = []
    left_index = right_index = 0

    # вычисляем длину каждого списка
    left_length = len(left)
    right_length = len(right)

    # идем по длине двух списков
    for _ in range(left_length + right_length):
        # если не вышли за границы списков
        if left_index < left_length and right_index < right_length:

            # сравнвиваем текущие элементы
            # если элемент в левом списке меньше
            if left[left_index] <= right[right_index]:
                ssorted.append(left[left_index])  # кидаем его в массив
                left_index += 1  # переходим к следующему элементу

            # если элемент правого списка меньше
            else:
                ssorted.append(right[right_index])  # добавляем его
                right_index += 1  # двигаемся по списку

        # если дошли до конца левого списка то добавляем все элементы в правом в конец результирующего
        elif left_index == left_length:
            ssorted.append(right[right_index])
            right_index += 1

        # тут наоборот
        elif right_index == right_length:
            ssorted.append(left[left_index])
            left_index += 1

    return ssorted

def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be ssorted
    :return: container ssorted in ascending order
    """

    if len(container) <= 1:
        return container

    # находим середину
    mid = len(container) // 2

    # сортируем левую и правую часть
    left = sort(container[:mid])
    right = sort(container[mid:])

    # сливаем две части в отсортированный массив
    container = merge(left, right)
    return container
