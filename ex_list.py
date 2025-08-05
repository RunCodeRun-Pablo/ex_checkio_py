# This function check within a bool list whether the majority of items are true

def is_majority(items: list[bool]) -> bool:
    t_num = items.count(True)
    f_num = items.count(False)
    return t_num > f_num


# This function accepts a list of ints and an int (N), you have to return the power of list.index(N)^N

