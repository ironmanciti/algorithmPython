import random

def qsort(qlist):
    lower = []
    higher = []
    sorted_list = []

    if len(qlist) < 1:
        return           # None returned

    center = qlist[-1]

    for element in qlist[:-1]:
        if element <= center:
            lower.append(element)
        else:
            higher.append(element)

    lower = qsort(lower)

    if  lower != None:
        sorted_list += lower

    sorted_list.append(center)

    higher = qsort(higher)
    if  higher  != None:
        sorted_list += higher

    return sorted_list

print(qsort([random.randrange(1, 10000) for _ in range(1000)]))

"""
학생 list 를 우수한 성적순으로 정렬
"""

students = [
        ('홍길동', 3.9, 2016303),
        ('김철수', 3.0, 2016302),
        ('최자영', 4.3, 2016301),
]

print(sorted(students, key=lambda x: x[1], reverse=True))

"""
dictionary 를 value 순으로 정렬
"""

dict = {'A' :5,'D' :7,'C' :3,'B' :2}

print(sorted(dict.items(), key=lambda kv: kv[1]))

