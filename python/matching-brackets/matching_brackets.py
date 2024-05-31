def is_paired(input_string):
    opening_brackets = {'[', '(', '{'}
    closing_brackets = {']', ')', '}'}
    brackets = dict(zip(closing_brackets, opening_brackets))  

    stack = []
    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or (brackets[char] != stack.pop()):
                return False
    return len(stack) == 0
    
    
    
