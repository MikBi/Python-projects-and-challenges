def blackjack(a, b, c):
    if a + b + c <= 21:
        return a + b + c
    elif a + b + c > 21:
        if a == 11 or b == 11 or c == 11:
            return (a + b + c) - 10
        else:
            return 'BUST'


print(blackjack(9, 9, 11))
