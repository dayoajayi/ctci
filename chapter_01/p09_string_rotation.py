'''
Assume you have a method isSubstring which checks if one word is a substring of another.
Given two string, s1 and s2, write code to check if s2 is a rotation of s1 using only one call 
to isSubstring(e.g. "waterbottle" is a rotation of "erbottlewat")

I: "CodingInterview", "erviewCodingInt"
O: True
C: Optimize
E: 
'''
def isSubstring(x1, x2):
    return x1 in x2

def is_rotation(s1, s2):
     return len(s1) == len(s2) and isSubstring(s1, s2+s2)

print(is_rotation('CodingInterview', 'erviewCodingInt'))
print(is_rotation('test', 'est'))
