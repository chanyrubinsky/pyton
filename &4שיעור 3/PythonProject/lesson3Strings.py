#1
def analyze_list(list):
    count = 0
    for i in list:
        count += 1
    my_set = set(list)
    sum_ = sum(list)
    dict_ = {
        "ones_numbers": my_set,
        "avg": sum_ / count,
        "max": max(list),
        "min": min(list)
    }
    return dict_


print(analyze_list([5, 6, 7, 8]))


#2

def filter_dict(d, threshold):
    l = []
    for i in d:
        if i.salary > threshold:
            l.append(i)
    return l


dict2 = {{'name': 'chani', 'salary': 766},
         {'name': 'fgh', 'salary': 76868}}

print filter_dict(dict2, 7)
