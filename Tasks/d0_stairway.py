from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    if len(stairway) == 0:
        return 0

    st_min = [0]*len(stairway)
    st_min[0] = stairway[0]
    st_min[1] = stairway[1]
    for st in range(2, len(stairway)):
        st_min[st] = min(st_min[st - 1], st_min[st - 2]) + stairway[st]
    print(st_min[-1])
    return st_min[-1]

def main():
    stairway = [1, 2, 3, 1, 2, 3]
    res = stairway_path(stairway)
    print(res)

if __name__ == "__main__":
    main()



"""Это ещё один вариант"""

def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    if len(stairway) == 0:
        return 0
    st_min = list(stairway[:2])
    st_min[0] = stairway[0]
    st_min[1] = stairway[1]
    for st in range(2, len(stairway)):
        st_min.append(min(st_min[-1], st_min[-2]) + stairway[st])
    return st_min[-1]

def main():
    stairway = [1, 2, 3, 1, 2, 3]
    res = stairway_path(stairway)
    print(res)

if __name__ == "__main__":
    main()

stairway = [1, 2, 3]
stairway_path(stairway)