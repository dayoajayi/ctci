# Given two strings, write a function to determine if one is a permutation of the other

# I: Two strings, e.g. "hiiiya", "hiya"
# O: 
# C: 
# E: 

def check_permutation(inputString1, inputString2):
    return len(set(inputString1)) == len(inputString2) or len(set(inputString2)) == len(inputString1)
    
print(check_permutation('hiya', 'hiiiiiya'))
