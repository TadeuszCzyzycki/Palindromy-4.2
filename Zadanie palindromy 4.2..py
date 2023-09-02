""" Zadanie palindromy 4.2"""

def is_palindrome(word):
    cleaned_word = word.lower()
    return cleaned_word == cleaned_word[::-1]



word_to_check = "Tenet"
if is_palindrome(word_to_check):
    is_palindrome = True
    print(is_palindrome)
else:
    is_palindrome = False
    print(is_palindrome)

