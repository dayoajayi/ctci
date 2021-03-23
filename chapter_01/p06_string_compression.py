'''
 Implement a method to perform basic string compression using the counts 
 of repeated characters. For example, the string aabcccccaaa would become 
 a2b2c5a3. If the "compressed" string would not become smaller than 
 the original string, your method should return the original string. 
 You can assume the string only has upper and lower case letters (Aa-Zz).

I: string
O: compressed string
C: if "compressed string" is not shoter, return original, only Aa-Zz
E: 


SOLUTION
********
 Begin by iterating through the string and counting the occurences of 
 each letter. As we count the occurences, we keep a separate string that 
 we will build up as we count the characters.

 

'''

def string_compression(input_string):
    compressed_string = ""
    count = 1
    
    for i in range(len(input_string) - 1):
        if input_string[i] == input_string[i+1]:
            count += 1
        else:
            compressed_string += input_string[i] + str(count)
            count = 1
    compressed_string += input_string[i+1] + str(count)

    if len(compressed_string) >= len(input_string):
        return input_string
    else:
        return compressed_string

print(string_compression('aabcccccaaa')) 
print(string_compression('aabccccca'))