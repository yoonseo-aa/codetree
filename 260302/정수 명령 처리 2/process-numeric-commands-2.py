N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
queue = []

for i in range(N):
    
    if command[i] == "push":
        queue.append(A[i])
        
    elif command[i] == "pop":
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
            
    elif command[i] == "size":
        print(len(queue))
        
    elif command[i] == "empty":
        if queue:
            print(0)
        else:
            print(1)
            
    elif command[i] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)