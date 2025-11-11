list = {"fjoirejti", "regf", "fd"}
list2 = [i for i in list if len(i)>3 ]

print(list2)


list3 = [1, 2, 3, 4, 5]
new_list3= [num if num % 3 == 0 else num * 2 for num in list3]


print(new_list3)

list4 = [2, 3, 5, 6, 8]
dict = {n: n*2 if n % 2 == 0 else "non" for n in list4}

print(dict)


str = "hgeiusjdsahflkja"
dict5 = {c: str.count(c) for c in str}

print(dict5)
