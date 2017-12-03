"""
Problem: (ZigZag Conversion)
---------
The string "PAYPALISHIRING" is written in a zigzag pattern on a 
given number of rows like this: (you may want to display this 
pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s): return s

        letters = [""] * numRows
        rowNum, step = 0, 1
    
        for character in s:
            letters[rowNum] += character
            if rowNum == 0:
                step = 1 # moving down the zigzag 
            elif rowNum == numRows - 1:
                step = -1
            rowNum += step
        
        return "".join(letters)

sol = Solution()
print(sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")

