def is_balanced(expression):
    opening_brackets = ['(', '{', '[']
    closing_brackets = [')', '}', ']']
    stack = []

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False
            else:
                position = closing_brackets.index(char)
                if stack.pop() != opening_brackets[position]:
                    return False

    if len(stack) == 0:
        return True
    else:
        return False
    
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False