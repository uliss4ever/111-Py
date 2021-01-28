from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """
    p = [0] * len(prefix_str)
    i = 1
    j = 0
    while i < len(prefix_str):
        if prefix_str[i] == prefix_str[j]:
            j += 1
            p[i] = j
            i += 1
        elif prefix_str[i] != prefix_str[j] and j != 0:
            j = p[j - 1]
        else:
            p[i] = 0
            i += 1
    return p

print(_prefix_fun("abbaabbab"))



def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """

    d = _prefix_fun(substr)
    i = j = 0
    while i < len(inp_string) and j < len(substr):
        if substr[j] == inp_string[i]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = d[j - 1]
    else:
        if j == len(substr):
            return i - j
        return None


if __name__ == "__main__":

    print(kmp_algo("akkkd", "ak"))
