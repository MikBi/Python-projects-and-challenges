st = 'Create a list of the first letters of every word in this string'

first = st.split()

myList = []

for f in first:
    myList += [value for (index, value) in enumerate(f) if index == 0]

print(myList)
