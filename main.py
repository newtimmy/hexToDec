from hex_calculator import hexCalculator

hex_object = hexCalculator("FF")

# Test 1
print(hex_object.calc_decimal_value_out_of_byte_list(hex_object.hex_to_dec(hex_object.hex_string)))

hex_object.hex_string = "00"

# Test 2
print(hex_object.calc_decimal_value_out_of_byte_list(hex_object.hex_to_dec(hex_object.hex_string)))

hex_object.hex_string = "GGGG"

# Test 3
print(hex_object.calc_decimal_value_out_of_byte_list(hex_object.hex_to_dec(hex_object.hex_string)))
