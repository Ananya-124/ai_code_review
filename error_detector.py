import ast

def detect_issues(code):
    tree, error = ast.parse(code) if isinstance(code, str) else (code, None)
    if error: return {"errors": [error]}

    defined_vars = set()
    used_vars = set()
    defined_imports = set()
    used_imports = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if isinstance(node.ctx, ast.Store):
                defined_vars.add(node.id)
            else:
                used_vars.add(node.id)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                defined_imports.add(alias.asname or alias.name)

    unused_vars = defined_vars - used_vars
    unused_imports = defined_imports - used_vars

    return {
        "unused_variables": list(unused_vars),
        "unused_imports": list(unused_imports)
    }