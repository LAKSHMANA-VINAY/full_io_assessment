
# 1) WAP to check if the given contact number is valid or invalid using regular expressions

import re
def valid_number(number):
    if '(' not in number:
        expression = r'^(\+?\d{0,2}[- ]?)?(\d{1,4}[-. ]?)?(\d{3,4}[-. ]?)?\d{3}[-. ]?\d{4}$'
    else:
        expression=r'^(\+?\d{0,2}[- ]?)?\(\d{3}\)[- ]?\d{3}-\d{4}$'
    if re.match(expression, number):
        return True
    else:
        return False
phone_numbers = ["2124567890","212-456-7890","(212)456-7890","(212)-456-7890","212.456.7890","212 456 7890","+12124567890","+1 212.456.7890","+212-456-7890","1-212-456-7890"]
for i in phone_numbers:
    if valid_number(i):
        print(f"{i} is a valid contact number")
    else:
        print(f"{i} is an invalid contact number")





