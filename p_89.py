from collections import OrderedDict

''' Find the number of characters saved by writing each of these in their minimal form. '''

roman_num_conv = OrderedDict([
    ('M', 1000), ('CM', 900), ('D', 500),
    ('CD', 400), ('C', 100), ('XC', 90),
    ('L', 50), ('XL', 40), ('X', 10),
    ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
])

def get_value(roman_num):
    value = roman_num_conv[roman_num[0]]

    prev_char = value
    for char in roman_num[1:]:
        char = roman_num_conv[char]
        if char > prev_char:
            char -= prev_char << 1
        value += char
        prev_char = char
    return value

def val_to_rn(num, string_lst):
    for char, val in roman_num_conv.iteritems():
        if num >= val:
            num -= val
            string_lst.append(char)
            if num:
                return val_to_rn(num, string_lst)
    return ''.join(string_lst)


with open("p089_roman.txt") as in_file:
    lines = in_file.read().splitlines()

print sum(len(line) - len(val_to_rn(get_value(line), [])) for line in lines)
