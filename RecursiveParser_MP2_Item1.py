"""
CMSC 124 Machine Problem 2 - Item #1
Topic Coverage: Syntax and Semantics 
Programmed by Dianne M. Mondido

<expr> ::= <expr> <operations> <variables> | <variables> | ~<variables> | (<expr>) 
<variables> ::= x | y | z
<operations> ::= + | - 
"""

VARIABLES = ['x','y','z']
PAR = ['(', ')']

class RecursiveParser():
    def __init__(self, input):    
        self.__source = input
        self.__currChar = None
        self.__currPos = -1
        self.__result = []  # Base Case. Stores valid characters
        self.nextChar()     # Goes to the first character of the string

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
    
    # Starting Non-Terminal
    def expr(self):
        self.__result = self.variable()
        while self.__currChar in ('+','-'):
            if self.__currChar == '+' and (self.peek() in VARIABLES or self.peek() == '~' or self.peek() in PAR):
                self.__result.append(self.__currChar)
                self.nextChar()
                self.variable()
            elif self.__currChar == '-' and (self.peek() in VARIABLES or self.peek() == '~' or self.peek() in PAR):
                self.__result.append(self.__currChar)
                self.nextChar()
                self.variable()
            else:
                return False
        return self.__result

    
    # Non-terminal
    def variable(self):
        # Reads if char is Digit or next char is ')'
        if (self.__currChar in VARIABLES and self.peek().isalpha() == False and self.peek().isdigit() == False and self.peek() != '(') or self.peek() ==')':
            if self.peek() == ')':
                self.__result.append(self.__currChar)
                self.nextChar()
                if self.peek() == '\0':
                    self.__result.append(self.__currChar)
                    return self.__result
                # If next char is ')', it goes to funtion variable()
                elif self.peek() == ')':
                    self.variable()
                # Else, it goes to next character
                else:
                    self.__result.append(self.__currChar)
                    self.nextChar()       
            else:
                self.__result.append(self.__currChar)
                self.nextChar()
        elif self.__currChar == '(' and (self.peek() in VARIABLES or self.peek() == '('):
            self.__result.append(self.__currChar)
            self.nextChar()
            self.expr()
            self.nextChar()
        elif self.__currChar == '~' and self.peek() in VARIABLES:
            self.__result.append(self.__currChar)
            self.nextChar()
            self.variable()
        else:
            return False
        return self.__result


while True:
    try:
        testCase = str(input())
        checkResult = RecursiveParser(testCase).expr()
        if checkResult != False:
            # Incase testCase have odd number and length of testCase and checkResult doesn't match, it immediately prints Invalid String
            if testCase.count('(') == testCase.count(')') and len(checkResult) == len(testCase):
                print ("Valid Input String")
                print(checkResult)
            else:
                print("Invalid Input String")
                print(checkResult)
        else:
            print("Invalid Input String")
    except:
        print("Invalid Input String")
        
            