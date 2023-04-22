from hex_calculator import hexCalculator
from dec_calculator import decCalculator

hex_object = hexCalculator("FF")

# Test 1
print(hex_object.calc_decimal_value_out_of_byte_list(hex_object.hex_to_dec(hex_object.hex_string)))

hex_object.hex_string = "00"

# Test 2
print(hex_object.calc_decimal_value_out_of_byte_list(hex_object.hex_to_dec(hex_object.hex_string)))

hex_object.hex_string = "GGGG"

# Test 3
print(hex_object.calc_decimal_value_out_of_byte_list(hex_object.hex_to_dec(hex_object.hex_string)))

dec_object = decCalculator("132")
# Test 4
print(dec_object.dec_to_hex(dec_object.dec_string))

dec_object = decCalculator("8A88")
# Test 5
print(dec_object.dec_to_hex(dec_object.dec_string))