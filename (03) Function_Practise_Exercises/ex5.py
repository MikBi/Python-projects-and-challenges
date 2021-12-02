def master_yoda(text):
    reverse = text.split()
    txt = ''
    for r in reversed(reverse):
        txt += r + ' '
    return txt


print(master_yoda('I am home'))
