def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def main():
    t = int(input())
    values = []
    for i in range(t):
        values.append(int(input()))

    for i in values:
        print(factorial(i))

main()