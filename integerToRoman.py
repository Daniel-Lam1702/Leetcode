class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbols = "IVXLCDM"
        roman = ""
        position = 1
        while(num != 0):
            digit = num % 10
            if position == 1:
                roman = self.convertToRoman(digit, symbols[:3]) + roman
            elif position == 10:
                roman = self.convertToRoman(digit, symbols[2:5]) + roman
            elif position == 100:
                roman = self.convertToRoman(digit, symbols[4:7]) + roman
            elif position == 1000:
                for i in range(digit):
                    roman = "M" + roman
            num /= 10
            position *= 10
        return roman
    def convertToRoman(self, digit, symbols):
        if digit == 4:
            return symbols[0] + symbols[1]
        elif digit == 9:
            return symbols[0] + symbols[2]
        elif digit < 4:
            string = ""
            for i in range(digit):
                string += symbols[0]
            return string
        else:
            string = symbols[1]
            for i in range(5, digit):
                string += symbols[0]
            return string