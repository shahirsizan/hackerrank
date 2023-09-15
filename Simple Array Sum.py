def simpleArraySum(ar):
    sum = 0

    for num in ar:
        sum += num

    return sum


n = int(input())
arr = list(map(int, input().split()[:n]))

result = simpleArraySum(arr)
print(result)
