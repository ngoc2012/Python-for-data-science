from typing import Iterable

def count_in_list(lst: Iterable, target: any) -> int:
    """ Returns the number of times target appears in lst """
    return len([x for x in lst if x == target])
