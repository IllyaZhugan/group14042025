import keyword
import string


def is_valid_variable_name(name):
    if name in keyword.kwlist:
        return False

    if not name:
        return False

    if name[0].isdigit():
        return False

    if name.count("_") > 1:
        return False

    for char in name:
        if (
            char in string.ascii_uppercase
            or (char in string.punctuation and char != "_")
            or char.isspace()
        ):
            return False

    return True


user_input = input()
print(is_valid_variable_name(user_input))

