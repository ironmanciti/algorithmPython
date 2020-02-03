import turtle

t = turtle.Turtle()
t.speed(1)

def drawTriangle(points):
    t.penup()
    t.setpos(points[0][0], points[0][1])
    t.pendown()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[0][0], points[0][1])

def getMid(p1, p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

def Sierpinski(points, n):
    drawTriangle(points)
    if n > 0:
        Sierpinski([points[0],
                    getMid(points[0], points[1]),
                    getMid(points[0], points[2])], n - 1)
        Sierpinski([points[1],
                    getMid(points[1], points[2]),
                    getMid(points[1], points[0])], n - 1)
        Sierpinski([points[2],
                    getMid(points[2], points[1]),
                    getMid(points[2], points[0])], n - 1)

def main():
    for i in range(10):
        Sierpinski([[0, 100], [-150, -100], [150, -100]], 3)
        turtle.clear()
    turtle.done()

if __name__ == "__main__":
    main()
    # t.penup()
    # t.setpos(150, -100)
    # t.pendown()
    # t.goto(0,100)
