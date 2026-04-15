def fibunacci_generator():
    x = 1
    y = 1
    z = 1
    yield 1

    while True:
     yield x+y
     z = x + y
     y=x
     x=z


generator = fibunacci_generator()

print(next(generator))
print(next(generator))
print(next(generator))

def enque_letters_generator (list_word):
    i = -1
    while list_word:
        i += 1
        yield set(list_word[i])


gen = enque_letters_generator(['hgfd','hgfd','jhkgfdddddddl'])

print(next(gen))
print(next(gen))
print(next(gen))

