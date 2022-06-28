class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = []
        letterPos = 0
        if(numRows == 1):
            return s
        for i in range(numRows):
            if(letterPos == len(s)):
                    break
            rows.append(s[i])
            letterPos += 1
        while(letterPos < len(s)):
            for j in range(numRows-2, -1, -1):
                if(letterPos == len(s)):
                    break
                rows[j] += s[letterPos]
                letterPos += 1
            for k in range(1,numRows):
                if(letterPos == len(s)):
                    break
                rows[k] += s[letterPos]
                letterPos += 1
        finalString = ""
        for i in range(len(rows)):
            finalString += rows[i]
        return finalString
        