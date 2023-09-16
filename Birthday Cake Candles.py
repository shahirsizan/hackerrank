def birthdayCakeCandles(candlesList):
    max_height = max(candlesList)
    count = candlesList.count(max_height)
    return count

n = int(input())
candlesList = list(map(int, input().split()))
result = birthdayCakeCandles(candlesList)
print(result)
