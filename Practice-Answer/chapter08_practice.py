"""
1)    ∑𝑛𝑘=1𝑘  을 계산하는 함수 sigma(n) 을 작성하라. (n 은 정수)
"""
def sigma(n):
    k = list(range(1, n+1))
    return sum(k)

print(sigma(10))

"""
2) xlist = [1, 2, 3, 4] 를 한줄에 출력하고 각 element 의 사이는 '/' 로 구분하라.
"""

xlist = [1, 2, 3, 4]

for n in xlist:
    print(n, end="/")

