class ArabicToRoman:
    def __init__(self):
        self.value_map = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        self.reverse_map = {}


    def convert(self, arabic):
        arabic = self.check_for_non_integer_values(arabic)
        if arabic > 3999 or arabic < 1:
            raise ValueError("This is not a valid integer for a Roman numeral")
        roman = self.create_conversion(arabic)
        return roman
    

    def create_conversion(self, arabic):
        roman = ""
        for value in self.value_map:
            while arabic >= value:
                roman += self.value_map[value]
                arabic -= value
        return roman
        

    def check_for_non_integer_values(self, arabic):
        arabic_float = float(arabic)
        arabic = int(arabic)
        if abs(arabic_float - float(arabic)) > 0.001:
            raise ValueError("This is not a valid integer for a Roman numeral")
        return arabic
    

    def make_reverse_map(self):
        for i in range(1, 4000):
            self.reverse_map[self.create_conversion(i)] = i
