from typing import iterable

def count_in_list(lst: iterable, target: any) -> int:
    """ Returns the number of times target appears in lst """
    return len([x for x in lst if x == target])
