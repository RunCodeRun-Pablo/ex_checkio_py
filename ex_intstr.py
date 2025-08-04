# Function to find the length of the longest longest substring without repeating characters within a given substring
# ie within pwwke it would be 3 (wke)

def longest_substr(s: str) -> int:

    first = result = 0
    chars = {}
    for ind, char in enumerate(s):
        if char in chars:
            first = max(first, chars[char] + 1)
        chars[char] = ind
        result = max(result, ind - first + 1)

    return result   # This function maintains a stable window of unrepeated chars all over the string


# Function to find the middle character of a string
# If the string is even it should return two characters
# If the string is odd it should return one character

def middle (text: str) -> str:
    l = len(text)
    if l % 2 == 0:
        return text[(l//2)-1:(l//2)+1]
    else:
        return text [(l//2)]



    