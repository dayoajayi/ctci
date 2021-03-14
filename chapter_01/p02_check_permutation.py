# Given two strings, write a function to determine if one is a permutation of the other

# I: Two strings, e.g. "hiiiya", "hiya"
# O: True/False
# C: Optimize
# E: empty string

def check_permutation(inputString1, inputString2):
    if len(inputString1) != len(inputString2):
        return False

    for char in inputString1:        
        if char in inputString2:
            inputString2 = inputString2.replace(char, '')
    return len(inputString2) == 0
    
print(check_permutation('hiiiiiya', 'hiya'))
print(check_permutation('', ''))
print(check_permutation('restful', 'fluster'))
print(check_permutation('car', 'bar'))