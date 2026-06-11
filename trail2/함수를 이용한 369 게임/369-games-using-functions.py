a, b = map(int, input().split())

# Please write your code here.
def is_369(num):
    return num % 3 == 0 or '3' in str(num) or '6' in str(num) or '9' in str(num)


answer = 0

for i in range(a, b + 1):
    if is_369(i):
        answer += 1

print(answer)