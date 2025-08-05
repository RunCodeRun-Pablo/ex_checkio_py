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


donuts = [0,1,2,0,4,0]
l = len(donuts)
print(donuts)

for n in donuts:
    while n < len(donuts):
        donuts.insert(donuts.index(n), 0)

print(donuts)
    