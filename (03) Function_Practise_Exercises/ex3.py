def makes_twenty(n1, n2):
    if n1 == 20 or n2 == 20:
        return True
    if n1 + n2 == 20:
        return True
    else:
        return False


print(makes_twenty(30, 10))
