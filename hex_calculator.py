class hexCalculator:
    def __init__(self, hex_string):
        self.hex_string = hex_string

    def hex_to_dec(self, hex_as_string):
        """

        :param hex_as_string:  hex parameter as string
        :return: dec paramenter as string
        """
        dec = []
        for character in hex_as_string:
            add_character = self.calc_hex_to_string(character)
            dec.append(add_character)
        return dec


    def calc_hex_to_string(self, character):
        """

        :param character: character like "A"
        :return: transformed character to hex value
        """
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
        if (switcher.get(character, "nothing") != "nothing"):
            return switcher.get(character, "nothing")
        else:
            return -1

    def calc_decimal_value_out_of_byte_list(self, byte_list):
        """

        :param byte_list: list of byte values
        :return: decimal number as string
        """
        decimal_number = 0
        count = 0
        for byte in byte_list:
            if(byte==-1):
                return "not a number"
            decimal_number += int(byte) * (16**(len(byte_list)-count-1))
            count += 1
        return decimal_number