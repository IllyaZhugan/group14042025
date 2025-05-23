import re

def first_word(text):
    match = re.search(r"[a-zA-Z']+", text)
    if match:
        return match.group(0)
    return ""


assert first_word("Hello world") == "Hello"
assert first_word("greetings, friends") == "greetings"
assert first_word("don't touch it") == "don't"
assert first_word(".., and so on ...") == "and"
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello"
print('OK')

