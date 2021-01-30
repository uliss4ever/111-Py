"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
# import networkx as nx

_root = { }

def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    current = _root

    if not current:
        current["key"] = key
        current["value"] = value
        current["right"] = {}
        current["left"] = {}
        return None


    while current:
        if key == current["key"]:
            current["value"] = value
            return None
        elif key > current["key"]:
            if not current["right"]:
                current["right"] = {"key": key, "value": value, "right": {}, "left": {}}
                return None
            print("go r")
            current = current["right"]
        else:
            if not current["left"]:
                current["left"] = {"key": key, "value": value, "right": {}, "left": {}}
                return None
            print("go l")
            current = current["left"]

    return None


def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    current = _root
    if not current:
        return None
    flag = False
    parent = current
    while current:
        if key < current["key"]:
            parent = current
            current = current["left"]
        elif key > current["key"]:
            parent = current
            current = current["right"]
        elif key == current["key"]:
            flag = True
            break

    if not flag:
        return None

    if not current["left"] and not current["right"]:
        r = (current["key"], current["value"])
        current.clear()
        return r

    if not current["left"] or not current["right"]:
        print("YES")
        r = (current["key"], current["value"])
        if parent["key"] == current["key"]:
            if not current["right"]:
                parent["key"] = current["left"]["key"]
                parent["value"] = current["left"]["value"]
                parent["left"] = current["left"]["left"]
            elif not current["left"]:
                parent["key"] = current["right"]["key"]
                parent["value"] = current["right"]["value"]
                parent["right"] = current["right"]["right"]
            return r

        if not current["left"]:
            if parent["left"] and parent["left"]["key"] == current["key"]:
                parent["left"] = current["right"]
            else:
                parent["right"] = current["right"]
        else:
            if parent["left"] and parent["left"]["key"] == current["key"]:
                parent["left"] = current["left"]
            else:
                parent["right"] = current["left"]
        return r

    print("YES")
    print(current)
    r = (current["key"], current["value"])
    current2 = _root
    next_key = _root
    while current2:
        if current2["key"] > current["key"]:
            next_key = current2
            current2 = current["left"]
        else:
            current2 = current2["right"]

    new_key = next_key["key"]
    new_value = next_key["value"]
    remove(next_key["key"])
    current["key"] = new_key
    current["value"] = new_value
    return r



def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """

    current = _root
    while True:
        if key == current["key"]:
            return current["value"]
        elif key > current["key"]:
            current = current["right"]
        else:
            current = current["left"]


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    while _root:
        remove(_root["key"])
    return None

def _find(key: int) -> Optional[Tuple[bool, dict]]:

    current_node = _root
    while current_node:
        if key == current_node["key"]:
            print("found")
            return (True, current_node)
        elif key > current_node["key"]:
            print("go right")
            current_node = current_node["right"]
        else:
            print("go left")
            current_node = current_node["left"]
    return (False, current_node)


if __name__ == "__main__":
    insert(0, "Never")
    insert(1, "gonna")
    insert(2, "give")
    insert(11, "you")
    insert(-3, "up")
    print(_root)
    clear()
    print(_root)