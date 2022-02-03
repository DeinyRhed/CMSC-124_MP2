"""
CMSC 124 Machine Problem 2 - Item #2
Topic Coverage: Syntax and Semantics 
Programmed by Dianne M. Mondido

Palindrome: pop, pop a pop, a but tuba 
Not a palindrome: hey, joe, the quick brown fox

<palindrome> ::= a <palindrome> a | b <palindrome> b | c <palindrome> c | … | z <palindrome> z | <letter> 
<letter> ::= a | b | c | … | z
"""
import re

class RecursiveParser():
    def __init__(self, input):    
        self.__source = input
        self.__currChar = None
        self.__currPos = -1
        self.__index = 0
        self.__strlength = len(self.__source)
        self.__firstHalf = ''  # Base Case. Stores first half characters of the string
        self.__secondHalf = '' # Base Case. Stores second half characters of the string
        self.nextChar()        # Goes to the first character of the string

    # Iterates over the string one-by-one
    def nextChar(self):
        self.__currPos += 1
        # Check if currPos has exceeded length of self.__source
        if self.__currPos >= len(self.__source):
            self.__currChar = '\0'
        else:
            self.__currChar = self.__source[self.__currPos]
    
    # Returns the next character of the self.__currChar
    def peek(self):
        if self.__currPos+1 >= len(self.__source):
            return '\0'
        return self.__source[self.__currPos+1]

    # Non-terminal. This function is recursive
    def palindrome(self):
        # self.__index counts the string starting from the end character up to the start character. Backward counting of string. 
        self.__index += -1
        # If current character == input[self.__index] is equal, string length is even, and current position count <= string length /2
        if self.__currChar == self.__source[self.__index] and self.__strlength % 2 == 0 and self.__currPos+1 <= self.__strlength/2:
            self.__firstHalf += self.__currChar
            self.__secondHalf += self.__currChar
            self.nextChar()
            self.palindrome()
        
         # If fcurrent character == input[self.__index], string length is odd and != 1, and current position count <= string length /2
        elif self.__currChar == self.__source[self.__index] and self.__strlength % 2 == 1 and self.__strlength != 1 and self.__currPos <= int(self.__strlength/2):
            if self.__currPos == int(self.__strlength/2):
                self.__firstHalf += self.__currChar
                self.nextChar()
                self.palindrome()
            else:
                self.__firstHalf += self.__currChar
                self.__secondHalf += self.__currChar
                self.nextChar()
                self.palindrome()

        # In case input is just one character
        elif self.__strlength == 1:
            self.__firstHalf += self.__currChar

    def reverseString(self):
        self.palindrome()
        self.__secondHalf = self.__secondHalf[::-1]
        return self.__firstHalf + self.__secondHalf


while True:
    try:
        checkResult = " "
        testCase = str(input()).replace(" ","").lower()
        # For removing unwanted characters
        testCase = re.sub(r'[.,"\'–?:!;]', '', testCase)
        checkResult = RecursiveParser(testCase.replace(" ","").lower()).reverseString()
        if testCase == checkResult:
            print("String is a PALINDROME")
        else:
            print("String is NOT A PALINDROME")
    except Exception as e:
        print("String is NOT A PALINDROME")
        
    
    del checkResult