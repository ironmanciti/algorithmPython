string = '.다니습있 수 할 을밍래그로프 nohtyP 는나'

# 1. 재귀적 방법
def recursive(s):
    if not s:
        return ''
    else:
        return s[-1] + recursive(s[:-1])

print(recursive(string))

# 2. for loop 과 string 연산 사용

sum = ''
for s in string:
    sum = s + sum

print(sum)

# Pythonic way
print(string[::-1])

"""
- lambda 를 이용하여 test_list 의 각 문장이 몇개의 단어로 이루어져 있는지 한줄 coding
"""
test_list = ['this is a book', 'good morning', 'apple', 'apple orange pear', 'hello python and functional programmiong']

for s in test_list:
    print((lambda x: len(x))(s.split(' ')))