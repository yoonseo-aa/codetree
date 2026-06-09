n, m = map(int, input().split())

# Please write your code here.
def lcm(n, m):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return n * m // gcd(n, m)

print(lcm(n, m))