def hex_to_dec(hex_as_string):
    dec = []
    for character in hex_as_string:
        add_character = calc_hex_to_string(character)
        dec.append(add_character)
    return dec

def calc_hex_to_string(character):
        switcher = {
            "0": "0",
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "A": "10",
            "B": "11",
            "C": "12",
            "D": "13",
            "E": "14",
            "F": "15"
        }
        return switcher.get(character, "nothing")

def calc_decimal_value_out_of_byte_list(byte_list):
    decimal_number = 0
    count = 0
    for byte in byte_list:
        decimal_number += int(byte) * (16**(len(byte_list)-count-1))
        count += 1
    return decimal_number

print(calc_decimal_value_out_of_byte_list(hex_to_dec("")))

# just a test
