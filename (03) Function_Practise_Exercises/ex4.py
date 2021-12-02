def old_macdonald(name):
    new_word = ''
    for index, letter in enumerate(name):
        if index == 0 or index == 3:
            new_word += letter.upper()
        else:
            new_word += letter
    return new_word


print(old_macdonald('macdonald'))
