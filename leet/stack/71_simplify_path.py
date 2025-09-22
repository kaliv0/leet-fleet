# 71. Simplify Path

def simplify_path(path: str) -> str:
    stack = []
    sub_path = ''
    for ch in path + '/':
        if ch == '/':
            if sub_path == "..":
                if stack:
                    stack.pop()
            elif sub_path and sub_path != ".":
                stack.append(sub_path)
            sub_path = ''
        else:
            sub_path += ch

    return '/' + '/'.join(stack)
