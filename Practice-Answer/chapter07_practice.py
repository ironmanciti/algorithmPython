"""
1) 다음 문장 수행 후의 output 은 ?
"""
xlist = [1, [1, 2], [1, 2, 3]]
print(xlist[1][1] + 1)

"""
2) xlist = [1, 2, 3, 4] 를 한줄에 출력하고 각 element 의 사이는 '/' 로 구분하라.
"""

xlist = [1, 2, 3, 4]

for n in xlist:
    print(n, end="/")

"""
3) 두개의 list element 들을 짝을 지워 출력
"""
stocks = ['삼성전자', '대한항공', 'google', 'apple']
close = [40000, 2000, 50000, 100000]

for s, c in zip(stocks, close):
    print(s, c)
