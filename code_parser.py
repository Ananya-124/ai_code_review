import ast

def parse_code(code):
    try:
        tree = ast.parse(code)
        return tree, None
    except SyntaxError as e:
        return None, f"Syntax Error at line {e.lineno}: {e.msg}"