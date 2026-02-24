N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
stack = []
def push_back(stack, n):
    stack.append(n)

def get(stack, n):
    return stack[n-1]

def size(stack):
    return len(stack)

def pop_back(stack):
    stack.pop()

for i in range(N):
    if command[i] == 'push_back':
        push_back(stack, num[i])
    elif command[i] == 'size':
        print(size(stack))
    elif command[i] == 'get':
        print(get(stack, num[i]))
    else:
        pop_back(stack)
