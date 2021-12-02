def has_33(nums):
    for index, num in enumerate(nums):
        if index > 0:
            if num == nums[index - 1]:
                return True
            elif index + 1 == len(nums):
                return False


print(has_33([1, 3, 1, 3]))
