class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = "" #Sets an empty substring
        length = 0 #Sets the value of the longest substring
        for letter in s: #Goes through every letter of the string s
            if letter not in substring: #If the letter is not in the substring. Then, add the letter
                substring += letter
            else: #If it is in the substring. Then update the length of the longest substring
                if len(substring) > length:
                    length = len(substring)
                #Restart the value of the substring in which it gets rid of the letters before the letter that is equal to the variable letter
                for i in range(len(substring)):
                    if(substring[i] == letter):
                        break
                substring = substring[i+1:len(substring)] + letter
        #Checks if the last substring is the biggest one
        if len(substring) > length:
            length = len(substring)
        return length