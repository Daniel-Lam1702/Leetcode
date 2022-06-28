class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x == 0):
            return 0
        number = abs(x)
        reversedNumber = 0
        while(number != 0):
            reversedNumber = reversedNumber * 10 + number % 10
            number /= 10
        reversedNumber *= x/abs(x)
        if(reversedNumber < (-2 ** 31) or reversedNumber > (2 ** 31) - 1):
            return 0
        return reversedNumber