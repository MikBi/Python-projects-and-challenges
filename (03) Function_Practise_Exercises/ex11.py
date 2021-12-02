def spy_game(nums):
    first = None
    second = None
    third = None
    reserve = None
    flag = False
    for x in nums:
        if x == 0 or x == 7:
            if first is None:
                first = x
            elif second is None:
                second = x
            elif third is None:
                third = x
        if reserve is not None and first is not None and second is not None:
            if reserve == 0 and first == 0 and second == 7:
                flag = True
                return flag
            else:
                reserve = None

        if first is not None and second is not None and third is not None:
            if first == 0 and second == 0 and third == 7:
                flag = True
                return flag
            else:
                reserve = third
                first = None
                second = None
                third = None
    if flag is False:
        return flag


print(spy_game([1, 7, 2, 0, 4, 5, 0, 6, 0, 8, 9, 1, 0, 3, 7]))
