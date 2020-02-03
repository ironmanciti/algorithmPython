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

# # Sierpinski Triangle

import turtle

t = turtle.Turtle()
t.speed(5)
t.pensize(5)

def drawTurtle(points):
    t.penup()
    t.setpos(points[0][0], points[0][1])
    t.pendown()
    t.color('red')
    t.goto(points[1][0], points[1][1])
    t.color('green')
    t.goto(points[2][0], points[2][1])
    t.color('blue')
    t.goto(points[0][0], points[0][1])

def getMid(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def Sierpinski(points, n):
    drawTurtle(points)
    if n > 0:
        Sierpinski([points[0],
                    getMid(points[0], points[1]),
                    getMid(points[0], points[2])], n-1)
        Sierpinski([points[1],
                    getMid(points[1], points[0]),
                    getMid(points[1], points[2])], n-1)
        Sierpinski([points[2],
                    getMid(points[2], points[1]),
                    getMid(points[2], points[0])], n-1)

Sierpinski([[0, 100], [-150, -100], [150, -100]], 3)

turtle.done()

"""
- lambda 를 이용하여 test_list 의 각 문장이 몇개의 단어로 이루어져 있는지 한줄 coding
"""
test_list = ['this is a book', 'good morning', 'apple', 'apple orange pear', 'hello python and functional programmiong']

for s in test_list:
    print((lambda x: len(x))(s.split(' ')))









