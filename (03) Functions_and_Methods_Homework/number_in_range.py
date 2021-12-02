def ran_check(num, low, high):
    if low > high:
        temp = low
        low = high
        high = temp
    if low <= num <= high:
        return True
    else:
        return False


print(ran_check(5, 10, 2))
