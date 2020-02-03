## Turtle Basic
# Python 의 simple Graphic Tool

import turtle

def main():

    t = turtle.Turtle()   # turtle object 생성

    t.forward(150)        # 150 unit 전진
    t.left(90)            # 90 도 좌회전
    t.forward(75)         # 75 unit 전진

    for i in range(4):
        t.forward(50)
        t.left(90)

    t.penup()
    t.left(150)
    t.forward(150)
    t.pendown()

    for i in range(3):
        t.forward(175)
        t.left(120)

    # 별 그리기
    for _ in range(5):   
        t.forward(300)
        t.right(144)

    turtle.done()

if __name__ == "__main__":
    main()