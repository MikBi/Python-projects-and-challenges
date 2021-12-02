def summer_69(arr):
    sumi = 0
    passing = False
    for num in arr:
        if num == 6:
            passing = True
        if num == 9:
            passing = False
        if not passing and num != 9:
            sumi += num
    return sumi


print(summer_69([2, 1, 6, 9, 11]))
