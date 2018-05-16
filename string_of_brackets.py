string = input("Enter the String\n")
stack = []
top = ' '
flag = -1
for char in string:
    if char in ['{','[','(']:
        if char == '{':
            stack.append('}')
            top = '}'
        elif char == '[':
            stack.append(']')
            top = ']'
        else:
            stack.append(')')
            top = ')'
    elif char in ['}',']',')']:
        if  top != char:
            flag=0
            print("Not in the Format")
            break
        else:
            stack.pop()
            if stack:
                top = stack[len(stack)-1]
            else:
                top = ' '
if not stack:
    print("In the Format")
elif flag == -1:
    print("Not in the format");
