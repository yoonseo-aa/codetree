N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.
stack = []
for i in range(N):
    if command[i] == 'push':
        stack.append(value[i])
    elif command[i] == 'top':
        print(stack[-1])
    elif command[i] == 'size':
        print(len(stack))
    elif command[i] == 'pop':
        print(stack.pop())
    elif command[i] == 'empty':
        if stack:
            print(0)
        else:
            print(1)

        