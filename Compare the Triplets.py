def compareTriplets(aliceList, bobList):
    alice_score = 0
    bob_score = 0

    for i in range(3):
        if aliceList[i] > bobList[i]:
            alice_score += 1
        elif aliceList[i] < bobList[i]:
            bob_score += 1

    return alice_score, bob_score

aliceList = list(map(int, input().split()))
bobList = list(map(int, input().split()))

result = compareTriplets(aliceList, bobList)
print(result[0], result[1])
