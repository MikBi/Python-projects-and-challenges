def up_low(s):
    letters = [char for char in s]
    capital = 0
    lower = 0
    for l in letters:
        if l.isalpha():
            if l.islower():
                lower += 1
            else:
                capital += 1
    print(f"No. of Upper case characters :  {capital}")
    print(f"No. of Upper case characters :  {lower}")


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
