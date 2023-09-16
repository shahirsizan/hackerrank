def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0

    for apple in apples:
        apple_position = a + apple
        if s <= apple_position <= t:
            apple_count += 1

    for orange in oranges:
        orange_position = b + orange
        if s <= orange_position <= t:
            orange_count += 1

    print(apple_count)
    print(orange_count)

s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())

apples = list(map(int, input().split()[:m]))
oranges = list(map(int, input().split()[:n]))

countApplesAndOranges(s, t, a, b, apples, oranges)
