from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    for i in range(len(container)):
        for j in range(1, len(container)):
            if container[j - 1] > container[j]:
                container[j - 1], container[j] = container[j], container[j - 1]
            print(container)
    return container

def main():
    print([1, 3, 5, 1, 3, 8, 5])
    sort([1, 3, 5, 1, 3, 8, 5])

if __name__ == "main":
    main()

