#!/usr/bin/env python3

def length_of_longest_substring(s):
    # create a dictionary to store the index of each character
    char_index = {}

    # initialize the start and max_length variables

    start = 0

    max_length = 0

    # iterate through the string
    for end, char in enumerate(s):
        # check if the character is already in the dictionary
        if char in char_index and char_index[char] >= start:
            # update the start variable
            start = char_index[char] + 1

        # update the index of the character
        char_index[char] = end

        # update the max_length variable
        max_length = max(max_length, end - start + 1)


    return max_length

#   TESTS

print(length_of_longest_substring(""))           # Output: 0
print(length_of_longest_substring("abcdef"))     # Output: 6
print(length_of_longest_substring("aabbcc"))     # Output: 2
print(length_of_longest_substring("abcbacbb"))   # Output: 3
print(length_of_longest_substring("dvdf"))       # Output: 3
print(length_of_longest_substring("anviaj"))     # Output: 5
print(length_of_longest_substring(" "))          # Output: 1
print(length_of_longest_substring("au"))         # Output: 2
print(length_of_longest_substring("aab"))        # Output: 2
print(length_of_longest_substring("abba"))       # Output: 2
print(length_of_longest_substring("tmmzuxt"))    # Output: 5
print(length_of_longest_substring("ohvhjdml"))   # Output: 6
print(length_of_longest_substring("jbpnbwwd"))   # Output: 4
print(length_of_longest_substring("asjrgapa"))   # Output: 6
