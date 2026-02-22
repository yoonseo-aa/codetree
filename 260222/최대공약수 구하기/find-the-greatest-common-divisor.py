n, m = map(int, input().split())


# Please write your code here.
def max_cf(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

print(max_cf(n, m))

