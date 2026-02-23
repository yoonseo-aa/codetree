n = int(input())

# Please write your code here.
def even_5(num):
    n = str(num)
    sum_v = int(n[0]) + int(n[1])

    if n % 2 == 0 and sum_v % 5 == 0:
        return "Yes"
    else:
        return "No"

print(even_5(n))
