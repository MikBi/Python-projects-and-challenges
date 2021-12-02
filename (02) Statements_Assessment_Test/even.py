st = 'Print every word in this sentence that has an even number of letters'

myList = st.split()

for s in myList:
    print(len(s))
    if len(s) % 2 == 0:
        print('even!')
