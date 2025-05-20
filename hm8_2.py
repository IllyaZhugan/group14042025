def is_palindrome(text):
    text = text.lower()
    clean_text = ""

    for c in text:
        if c.isalnum():
            clean_text += c

    return clean_text == clean_text[::-1]


assert is_palindrome("A man, a plan, a canal: Panama") == True
assert is_palindrome("0P") == False
assert is_palindrome("a.") == True
assert is_palindrome("aurora") == False
print("ОК")
