str = input()

# Please write your code here.
stack = []
for ch in str:
    if ch == '(':
        stack.append('(')
    else:
        stack.pop()

if stack:
    print('No')
else:
    print('Yes')
