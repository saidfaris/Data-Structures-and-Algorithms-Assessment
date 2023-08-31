def is_balanced(expression):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False  # Closing bracket with no corresponding opening bracket
            top = stack.pop()
            if opening_brackets.index(top) != closing_brackets.index(char):
                return False  # Mismatched brackets
    return not stack  # True if the stack is empty (all brackets are balanced)

# Test cases
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
