"""
tuple element 로 구성된 list 에서 tuple 의 첫번째 element 가  'a' 인 tuple 이
alist 의 몇번째  element 인지 구하라. 단, for loop 과 비교문을 사용하지 않고 list comprehension 을 사용
"""
alist = [('x', 4), ('s', 5), ('a', 4), ('t', 5), ('k', 4), ('w', 5), ('a', 4)]

print([idx for idx, tup in enumerate(alist) if tup[0] == 'a'])

