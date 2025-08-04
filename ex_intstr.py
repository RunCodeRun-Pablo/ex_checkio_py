 # Function to findg the length of the longest longest substring without repeating characters within a given substring
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


    