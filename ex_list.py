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

# This function returns the same sentence but with the backwards words

def backward_string_by_word(text:str) -> str:
    return " ".join(word[::-1] for word in text.split(" "))

# This function returns the difference between a minimum and a maximum value. To consider: the substraction should only happens if the minimum value is before the maximum within the list index, else the function should return 0 

def stock_profit(stock: list[int]) -> int:
    if len(stock) < 2:
        return 0
    
    min_value_idx = stock.index(min(stock))
    post_min_prices = stock[min_value_idx+1:]

    if not post_min_prices:
        return 0
    
    benefit = max(post_min_prices) - min(stock)
    return max(benefit,0)

# This function eliminates consecutive duplicate elements

def compress(items: list[int]) -> Iterable[int]:
    new_items = []
    l = len(items)
    if l > 1:
        for n in range(l-1):
            if items[n] != items[n+1]:
                new_items.append(items[n])
        new_items.append(items[l-1])
    elif l == 1:
        return items
        
    return new_items

# I included this as an alternative answer (not mine) using a generator, which i found interesting, for obtaining the complete result you have to call the generator with a list

def compress(items: list[int]) -> Iterable[int]:

    for ind, val in enumerate(items):
        if not ind or val != items[ind - 1]:
            yield val

# Example of function calling : list(compress([]))

# This function given a list and an edge, we have to return a new list only with the elements within that edge, for example [1,2,3,4,5] and edge 3: should return [1,2,3]
# If the edge is not found in the list it should return the same list

def remove_all_after(items:list[int], border: int) -> Iterable[int]:
    return items[:items.index(border)+1] if border in items else items


# This function indicates with bools whether a list is composed of ordered increasing int items, if yes returns true, if not false.

def is_ascending(items: list[int]) -> bool:
    if not items:
        return True
    
    l, index = len(items),0
    for item in items:
        if index < l-1 and item < items[index+1]:
            index += 1
    return index == l-1

# Another version that could work also

def is_ascending(items: list[int]) -> bool:
    for i in range(len(items)-1):
        if items[i] >= items[i+1]:
            return False
    return True

# Given a str list and a str, you have to check if the str in the list appear in the same order as in the input str
# This function should return a bool value, example: ['hello','world'], 'is hello a word of the world' -> True

def words_order(text: str, words: list) -> bool:
    results = {i for i in text.split() if i in words}
    return sorted(results, key=text.index) == words

# This function gets a string as an input and outputs the number of empty lines it has (\n)

def non_empty_lines(text: str) -> int:
    text = [line.replace(" ", "") for line in text.split("\n")]
    text = [line for line in text if line]
    return len(text)





            










    






    















    



