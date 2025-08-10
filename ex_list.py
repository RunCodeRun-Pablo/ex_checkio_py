from _collections_abc import Iterable


# This function check within a bool list whether the majority of items are true

def is_majority(items: list[bool]) -> bool:
    t_num = items.count(True)
    f_num = items.count(False)
    return t_num > f_num


# This function accepts a list of ints and an int (N), you have to return the power of list.index(N)^N

def index_power(ar: list[int], n: [int]) -> int:
    if n <= len(ar)-1:
        return ar[n]**n
    else:
        return -1

# This function returns the sum of a list[even] numbers and multiplies the sum by the last item of the list (just accepts int list)

def checkio(array: list[int]) -> int:
    if not array:
        return 0
    res = sum(array[::2])
    return res*array[-1]

# This functions encounters zeros and duplicates them, the output is a new list with the duplicated 0

def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    return [x for n in donuts for x in ([0,0] if n == 0 else [n])]
duplicate_zeros([0,1,0])

# This functions defines the median of a list either even or odd

def median(data: list[int]) -> int | float:
    data.sort()
    l = len(data)
    mid = l//2
    if l % 2 == 0:
        return (data[mid-1]+data[mid])/2
    else:
        return data[mid]
    
# This functions separates elements in a tuple / list and concatenates it in a new string. Specifically it also changes any right string into left

def left_join(phrases: tuple[str, ...]) -> str:
    res = [x for item in phrases for x in ([item.replace("right","left")] if "right" in item else [item])]
    return ",".join(res)

# This function calculates the ending coordinates using a string in which f = forward, b = backward, l = left and r = right, considering a cartesian plot and starting in pos = 0,0

def follow(instructions: str) -> tuple[int, int] | list[int]:
    coords =["f","b","r","l"]
    x = 0
    y = 0
    for n in instructions:
        if n in coords and n == "f":
            y += 1
        elif n in coords and n == "b":
            y += -1
        elif n in coords and n == "r":
            x += 1
        elif n in coords and n == "l":
            x += -1
    return [x,y]

    



