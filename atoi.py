class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        negative = False
        number = 0
        for i in range(len(s)):
            if(s[i] != " " and (s[i].isalpha() or s[i] == ".")):
                break
            elif(s[i].isdigit()):
                number = 10 * number + int(s[i])
            elif(i != 0 and (s[i] in " -+." or s[i].isalpha()) and s[i-1].isdigit()):
                break
            elif(i != len(s) - 1 and (s[i] == "+" or s[i] == "-") and not s[i+1].isdigit()):
                break
            elif(s[i] == "-"):
                negative = True
        if negative:
            number *= -1
            if(number < -2 ** 31):
                number = -2 ** 31
        else:
            if(number > 2 ** 31 - 1):
                number = 2 ** 31 - 1
        return number