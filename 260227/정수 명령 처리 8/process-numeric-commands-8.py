from collections import deque
N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        A.append(int(line[1]))
    else:
        A.append(0)

arr = []
# Please write your code here.
for i in range(len(command)):
    if command[i] == 'push_back':
        arr.append(A[i])
    elif command[i] == 'push_front':
        arr.insert(0,A[i])
    elif command[i] == 'pop_front':
        print(arr.pop(0))
    elif command[i] == 'pop_back':
        print(arr.pop())
    elif command[i] == 'size':
        print(len(arr))
    elif command[i] == 'front':
        print(arr[0])
    elif command[i] == 'back':
        print(arr[-1])
    else:
        if arr:
            print(0)
        else:
            print(1)