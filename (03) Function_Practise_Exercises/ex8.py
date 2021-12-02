def paper_doll(text):
    three_times_letter = ''
    for letter in text:
        three_times_letter += 3*letter
    return three_times_letter


print(paper_doll('Hello'))
