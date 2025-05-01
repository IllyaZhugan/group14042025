# some_string =  'I live in Odesa since 2004'
#
# other_result = some_string.split('i')
# other_result_visual = ['I', 'live', 'in', 'Odesa', 'since', '2004']
#
# empty_list = []
#
# if empty_list:
#     print(5555555555)
#
# not_empty_list = ['4545', 5555,  5.5, True, False, [55], empty_list]
# if not_empty_list:
#     print(2222222222)
#
# fifth_elem = not_empty_list[4]
# # big_elem = not_empty_list[40]
# fifth_letter = some_string[4]
#
# len_list - len(not_empty_list)
# len_list2 - len(empty_list)
# len_string - len(some_string)

purchase_plan = ['banana']

# add 1 elem
purchase_plan.append('salt')
purchase_plan.append('salt')
purchase_plan.append('2')
purchase_plan.append('')


# merge by another list
sister_plan = ["bread", "milk"]
purchase_plan.extend(sister_plan)
# purchase_plan.extend("5565656565")

purchase_plan.sort()
# purchase_plan.sort(reverse=True)
# purchase_plan.sort(key=len, reverse=True)

# delete item
purchase_plan.remove("salt")

if "nails" in purchase_plan:
    purchase_plan.remove("nails")

if 'abc' in 'abcd':
    print(32323232)


# delete by index
purchase_plan.pop()
purchase_plan.pop(0)


pass