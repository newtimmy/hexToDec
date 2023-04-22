import math

class decCalculator:
    def __init__(self, dec_string):
        self.dec_string = dec_string

    def dec_to_hex(self, dec_as_string):
        """

        :param hex_as_string:  hex parameter as string
        :return: dec paramenter as string
        """

        try:
            dec = int(dec_as_string)
        except:
            return "No decimal number given"
        hex = ""
        while(dec>0):
            rest = dec%16
            hex = self.calc_dec_to_string(str(rest)) + hex
            dec = math.floor(dec/16)
        return hex

    def calc_dec_to_string(self, character):
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
            "10": "A",
            "11": "B",
            "12": "C",
            "13": "D",
            "14": "E",
            "15": "F"
        }
        if (switcher.get(character, "nothing") != "nothing"):
            return switcher.get(character, "nothing")
        else:
            return -1
