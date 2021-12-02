st = 'Print only the words that start with s in this sentence'
words = st.split()
x = 1

for w in words:
    for word in w:
        if word == 's' or word == 'S':
            break
        if x == len(w):
            print(w)
        x += 1
    x = 1
