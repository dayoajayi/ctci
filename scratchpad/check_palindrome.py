def check_palindrome(str):
    str = str.replace(' ', '')
    
    # base case
    if len(str) == 0:
        return True

    for char in str:
        