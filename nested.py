#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "astephens91"

import sys

def areBracketsNestedCorreclty(filename):
    fwrite = open("output.txt", "a+")
    
    fread = open(filename, "r")
    text =fread.read()
    
    stack = []


    for i in range(len(text)):
        if text[i] == '(' and text[i+1] == '*':
            stack.append(text[i] + text[i+1])
        elif (text[i] == '(' or text[i] == '[' or text[i] == '{'):
            stack.append(text[i])
            continue
            
        if (len(stack) == 0):
            fwrite.write("YES" + "\n")
        
        if text[i] == '*' and text[i+1] == ')':
            x = stack.pop()

            if (x == '(' or x == '[' or x == '{'):
                fwrite.write("NO " + str(text.index(text[i])) + "\n")

        elif text[i] == ')' and text[i-1] != '*':
            x = stack.pop()
        
            if (x == '{' or x == '[' or x =='(*'):
                fwrite.write("NO " + str(text.index(text[i])) + "\n")
        
        elif text[i] == '}':
            x = stack.pop()
            
            if (x == '(' or x == '[' or x== '(*'):
                fwrite.write("NO " + str(text.index(text[i])) + "\n")
        
        elif text[i] == ']':
            x = stack.pop()

            if (x == '(' or x == '{' or x == '(*'):
                fwrite.write("NO " + str(text.index(text[i])) + "\n")
    if len(stack):
        fwrite.write("YES" + "\n")
    
    




def main(args):
   
    areBracketsNestedCorreclty("input.txt")
    """Add your code here"""

if __name__ == '__main__':
    main(sys.argv)
