# Write a method to replace all spaecs in a string with '%20'. You may assume that 
# the string has sufficient space at the end to hold the additional character,
# and that you are given the "true" length of the string
# 
# EXAMPLE: 
# Input: "Mr John Smith", 13
# Output: "Mr%20John%20Smith"

def urlify(inputString, wordCount):
    return inputString.replace(' ', '%20')

print(urlify('Mr John Smith',13))
