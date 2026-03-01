s = input()

stack = []
for ch in s:
    if ch == '(':
        stack.append('(')
    else: 
        if not stack:  
            print("No")
            break
        stack.pop()
else:
    if stack:
        print("No")
    else:
        print("Yes")