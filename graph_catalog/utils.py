from collections.abc import Callable
from typing import Any


def binary_search(
    l: list[Any], item: Any, key: Callable[[Any], Any] = lambda item: item
) -> tuple[bool, int]:

    lower = 0
    higher = len(l) - 1

    isFound = False

    while lower <= higher:
        mid = (lower + higher) // 2
        middle_value = key(l[mid])
        insert_value = key(item)
        if insert_value < middle_value:
            higher = mid - 1
        elif middle_value < insert_value:
            lower = mid + 1
        else:
            isFound = True

    return (isFound, lower)


print(binary_search([[-1], [0], [3], [4], [8], [13]], [7], key=lambda x: x[0]))
