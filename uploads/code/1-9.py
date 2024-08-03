n = int(input())

def fatorial(n):
    if n == 1:
       return n
    return n * fatorial(n-1)

print(fatorial(n))