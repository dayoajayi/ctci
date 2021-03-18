'''
 There are three types of edits that can be performed on strings: insert a character, 
 remove a character, or replace a character. Given two strings, write a function to 
 check if they are one edit (or zero edits) away

I: Two strings 
O: True/False
C: Optimize
E: 

'''
def one_away(inputString1, inputString2):
    dictionary = {}
    diffs = {}

    if len(inputString1) != len(inputString2):
        return False

    for char in inputString1:
        if char in inputString2:
            dictionary[char] = dictionary.get(char, 0) + 1
        else:
            diffs[char] = dictionary.get(char, 0) + 1
    if len(diffs) >= 1:
        return False
    else:         
        #print (f'dictionary: {dictionary}')
        #print (f'diffs: {diffs}')
        return True


print(one_away('care', 'bare'))
print(one_away('rake', 'rake'))
print(one_away('whale', 'wrale'))
