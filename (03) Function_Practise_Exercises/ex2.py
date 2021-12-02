def animal_crackers(string):
    animal = string.split()
    word_a = animal[0].lower()
    word_b = animal[1].lower()
    if word_a[0] == word_b[0]:
        return True
    else:
        return False


print(animal_crackers('Crazy Kangaroo'))



