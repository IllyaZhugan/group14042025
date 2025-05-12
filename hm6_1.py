import string

user_input = input()

start_char, end_char = user_input.split("-")
start_index = string.ascii_letters.index(start_char)
end_index = string.ascii_letters.index(end_char)

result = string.ascii_letters[start_index : end_index + 1]

print(result)

