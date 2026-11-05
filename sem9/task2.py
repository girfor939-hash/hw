def rpn_calculator(expression):
    if not expression.strip():
        return "некорректно"
        
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token in ('+', '-', '*', '/'):
            if len(stack) < 2:
                return "некорректно"
            
            b = stack.pop()
            a = stack.pop()
            
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/':
                if b == 0:
                    return "некорректно"
                stack.append(a / b)
        else:
            try:
                stack.append(float(token)) 
            except ValueError:
                return "некорректно"
                
    if len(stack) == 1:
        return stack[0]
    else:
        return "некорректно"
