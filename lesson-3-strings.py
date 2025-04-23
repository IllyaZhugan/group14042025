some_string = "om\n5       my name is igor HHHHHHHH 666666666665454545 namer  "

upper = some_string.upper()  # 'MY NAME IS IGOR 666666666665454545'
lower = some_string.lower()  # 'my name is igor hhhhhhhh 666666666665454545'
title = some_string.title()  # 'My Name Is Igor Hhhhhhhh 666666666665454545'
capitalize = some_string.capitalize()  # 'My name is igor hhhhhhhh 666666666665454545'
chain = some_string.lower().upper().capitalize()

clear_string_space = some_string.strip()
clear_string_symbol = some_string.strip(" 53")
clear_string_symbol_left = some_string.lstrip(" 54name")
clear_string_symbol_right = some_string.rstrip(" 54namer")


change_inner_text = (
    some_string.replace("name", "surname", 1)
    .replace("igor", "Igor")
    .replace("namer", "")
    # .replace("6", "5")
    # .replace("5", "6")
)

table = str.maketrans("65", "56", "\n")
result_smart_change = some_string.translate(table)


slices1 = some_string[:]
slices2 = some_string[0:12]
slices3 = some_string[12:20]
slices4 = some_string[::2]  # кожен другий символ
slices5 = some_string[1:25:2]  # кожен другий символ
slices6 = some_string[::-1]  # revers
slices7 = some_string[::-2]  # revers
slices8 = some_string[-3:-20:-2]  # revers


pass
