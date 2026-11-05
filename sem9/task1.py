class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

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

def to_postfix_tokens(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
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
            if stack:
                stack.pop()
        else:
            while (stack and stack[-1] != '(' and 
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
    while stack:
        output.append(stack.pop())
    return output

def build_tree(postfix_tokens):
    stack = []
    for token in postfix_tokens:
        if token in "+-*/":
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(token, left, right))
        else:
            stack.append(Node(token))
    return stack[0]

def get_prefix(node):
    if node.value in "+-*/":
        return node.value + " " + get_prefix(node.left) + " " + get_prefix(node.right)
    return node.value

def get_postfix(node):
    if node.value in "+-*/":
        return get_postfix(node.left) + " " + get_postfix(node.right) + " " + node.value
    return node.value

def convert_expression(expr):
    tokens = tokenize(expr)
    postfix_tokens = to_postfix_tokens(tokens)
    root = build_tree(postfix_tokens)
    return get_prefix(root), get_postfix(root)
