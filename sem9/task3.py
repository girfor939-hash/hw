def tokenize(expr):
    tokens = []
    num = ""
    for char in expr:
        if char.isdigit() or char == '.':
            num += char
        else:
            if num:
                tokens.append(num)
                num = ""
            if char in "+-*/()":
                tokens.append(char)
    if num:
        tokens.append(num)
    return tokens

def shunting_yard(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    tokens = tokenize(expression)
    output = []
    stack = []
    
    for token in tokens:
        if token not in "+-*/()":
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack or stack[-1] != '(':
                return "Ошибка: несбалансированные скобки"
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and 
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
            
    while stack:
        if stack[-1] == '(':
            return "Ошибка: несбалансированные скобки"
        output.append(stack.pop())
        
    return " ".join(output)
