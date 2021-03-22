'''
 There are three types of edits that can be performed on strings: 
    - insert a character, 
    - remove a character, or replace a character. 
    
    Given two strings, write a function to check if they are one edit (or zero edits) away

********
SOLUTION
********
We can start by first checking the lengths of both strings. If the lengths differ by more than 1, 
    we can immediately return False

Then, we iterate through both strings and compare them character-by-character, using pointers p1, p2

    - if the characters are the same, continue on to the next character for both strings
    - elif the characters are difference and we haven't made an edit yet
        - if the lenghts are the same
            - try replacing the character at String A with the char and string B
        - elif the lenghts are different, 
            - try deleting a char from the longer string
        - make a note that we've made an edit
    - elif the characters are different and we have made an edit
        return False

'''
def one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    p1,p2 = 0,0
    madeEdits = False

    while p1 < len(s2) and p2 < len(s2):
        if s1[p1] == s2[p2]:
            p1 += 1
            p2 += 1
        elif not madeEdits:
            madeEdits = True
            if len(s1) == len(s2):
                p1 += 1
                p2 += 1        
            elif len(s1) < len(s2):
                p2 += 1
            elif len(s1) > len(s2):
                p1 += 1
        else:
            return False
    return True


print(one_away('', '') == True)             
print(one_away('p', '') == True)            
print(one_away('care', 'bare') == True)     
print(one_away('abc', 'acs') == False)      
print(one_away('whale', 'wrale') == True)   