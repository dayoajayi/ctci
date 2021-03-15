'''
 Given a string, write a function to check if it is a permutation 
 of a palindrome. A palindrome is a word or phrase that is the same 
 forwards and backwards. A permutation is a rearrangement of letters.
 The palindrome does not need to be limited to just dictionary words.
 You can ignore casing and non-letter characters.
 
 EXAMPLE 
 Input: Tact Coa
 Output: True (permutations: 'taco cat' 'acto cta', etc...) 

 Input: Race Car
 Output: True (permutations: 'racecar') 

ANALYSIS: First, observe the characteristics of a palindrome: 
    the string either has to be even number of characters, or 
    an odd number of characters where one character appears
    only once in the middle.

    With this in mind, we can count the number of characters and determine 
    if our condition is met...

NOTE: There is a slight difference between this problem and that of 
    determining if the input string is a palindrome
'''

def palindrome_permutation(inputString):
    inputString = inputString.replace(' ', '')
    inputString = inputString.lower()

    dictionary = {}
    for char in inputString:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    
    odd_count = 0
    for key, value in dictionary.items():
        if value % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif value % 2 != 0 and odd_count != 0:
            return False
    return True

print(palindrome_permutation(' '))
print(palindrome_permutation('Race car'))
print(palindrome_permutation('Tact coa'))
print(palindrome_permutation('Race cart'))