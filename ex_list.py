from _collections_abc import Iterable
from typing import List, Any


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
    moves ={
        'f' : (0,1),
        'b' : (0,-1),
        'r' : (1,0),
        'l' : (-1,0)
    }
    x,y = 0,0
    for coords in instructions:
        if coords in moves:
            dx,dy = moves[coords]
            x += dx
            y += dy

    return x,y

# This function returns the same input list but changing the first item to the last position

def replace_first(items: list) -> Iterable:
    if len(items) >= 2:
        return items[1:] + items[:1]
    return items
        
# This function detects whether all the elements of a list are equal

def all_the_same(elements: list) -> bool:
    if elements:
        return elements.count(elements[0]) == len(elements)
    else:
        return True

# THis function returns the same sentence but with the backwards words

def backward_string_by_word(text:str) -> str:
    return " ".join(word[::-1] for word in text.split(" "))
    










    



