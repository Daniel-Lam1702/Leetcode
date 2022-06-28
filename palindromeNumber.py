class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0):
            return False
        if(x == 0):
            return True
        number = x
        reversedNumber = 0
        while(number != 0):
            reversedNumber = reversedNumber * 10 + number % 10
            number /= 10
        return reversedNumber == x