# Check Weather a tuple is a palindrome
tuple_palindrome = (1,22,22,21) 
pal = tuple_palindrome[::-1] == tuple_palindrome
tt = False
if not pal:
    pal = "not"
    tt = True
print("Original Tuple:", tuple_palindrome, "\n\n The tuple is", ("not a Palindrome" if tt else "a Palindrome"))