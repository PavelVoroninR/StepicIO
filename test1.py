def brackets(code_string: str = None):
    if code_string is None:
        raise Exception("String is empty")
    else:
        op_br_stack = []
        pos = 0

        for i in range(len(code_string)):
            print('pointer: ', i, '\tstack: ', op_br_stack, ' val: ', code_string[i])

            if code_string[i] in ['(', '[', '{']:
                pos = i
                op_br_stack.append((code_string[i], i))
                continue
            elif code_string[i] in [')', ']', '}']:
                pos = i
                if len(op_br_stack) == 0:
                    return i + 1
                if code_string[i] == ')' and op_br_stack[-1][0] == '(':
                    op_br_stack.pop()
                elif code_string[i] == ']' and op_br_stack[-1][0] == '[':
                    op_br_stack.pop()
                elif code_string[i] == '}' and op_br_stack[-1][0] == '{':
                    op_br_stack.pop()
                else:
                    return i + 1

        if len(op_br_stack) == 0:
            return 'Success'
        if len(op_br_stack) != 0:
            return op_br_stack[-1][1]+1

a = input()
print(brackets(a))
