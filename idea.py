    # while i <= len(text):
    #     # Group up the checks for '(*' and '*)'
    #     if i != (len(text) - 1):

    #         if text[i] == '(' and text[i+1] == '*':
    #             stack.append(text[i] + text[i+1])

    #         if text[i] == '*' and text[i+1] == ')' and text[i-1] != '(':
    #             if len(stack) > 0:
    #                 if stack[-1] == '(*':
    #                     stack.pop()
    #                 else:
    #                     fwrite.write("NO " + str(i - 1) + '\n')
    #     else:
    #         if (text[i] == '(' or text[i] == '[' or text[i] == '{' or text[i] == '<'):
    #             stack.append(text[i])
    #         # This does not care about checking ahead so it can be outside the sentinel 
    #         # # Looks like the rest from here can be outside it                        
    #         elif text[i] == ')':
    #             if len(stack) > 0:
    #                 if stack[-1] == '(':
    #                     stack.pop()
    #                 else:
    #                     fwrite.write("NO" + str(i - 1) + '\n')
    #         elif text[i] == ']':
    #             if len(stack) > 0:
    #                 if stack[-1] == '[':
    #                     stack.pop()
    #                 else:
    #                     fwrite.write("NO " + str(i - 1) + '\n')
    #         elif text[i] == '}':
    #             if len(stack) > 0:
    #                 if stack[-1] == '{':
    #                     stack.pop()
    #                 else:
    #                     fwrite.write("NO " + str(i - 1) + '\n')
    #         elif text[i] == '>':
    #             if len(stack) > 0:
    #                 if stack[-1] == '>':
    #                     stack.pop()
    #                 else:
    #                     fwrite.write("NO " + str(i - 1) + '\n')
            
    #         elif text[i] == '\n' and len(stack) == 0:
    #             fwrite.write("YES" + '\n')
    #             stack = []
    #         elif text[i] == '\n':
    #             stack = []
        
    #     i += 1