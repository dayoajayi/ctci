# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# I: string
# O: True/False
# C: no additional data structures, optimize
# E: empty string


class Solution(object):
    def is_unique(inputString):
        set_of_unique_characters = {}
        for char in inputString:
            if char in set_of_unique_characters:
                return False
            else:
                set_of_unique_characters[char] = 1
        return True

    def is_unique_pythonic(inputString):
        return len(set(inputString)) == len(inputString)

    print(is_unique("aaaaaa"))
    print(is_unique("abcdefg"))
    print(is_unique(""))
    print(is_unique("abcdefghijklmnopqrstuvwxyzz"))
    print(is_unique("abcdefghijklmnopqrstuvwxyz"))
    print("-------------------------------------")
    print(is_unique_pythonic("aaaaaa"))
    print(is_unique_pythonic("abcdefg"))
    print(is_unique_pythonic(""))
    print(is_unique_pythonic("abcdefghijklmnopqrstuvwxyzz"))
    print(is_unique_pythonic("abcdefghijklmnopqrstuvwxyz"))
