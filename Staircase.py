def staircase(n):
    for i in range(1, n+1):
        spaces = " " * (n-i)
        symbols = "#" * i
        print(spaces + symbols)

n = int(input())
staircase(n)
