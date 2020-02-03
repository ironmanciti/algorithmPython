"""
Python GUI tool 을 이용한 MAZE 작성
1. tkinter 기본 사용법 습득
2. OOP 를 통한 MAZE 그리기
"""

import tkinter as tk

# window object 생성
window = tk.Tk()
# window title
window.title("알고리즘으로 배우는 파이썬")   
# 배경색 지정
window.configure(background="black")
# WINDOW SIZE
window.geometry('800x800') # window size
# image 표시
photo1 = tk.PhotoImage(file="test.png")
tk.Label(window, image=photo1, bg="black").pack(side="top", anchor="w")  

# Label 생성
tk.Label(window, text="파이썬의 GUI 프로그램", bg="black", fg="white", font="none 15 bold").pack()
# canvas 생성
canvas = tk.Canvas(window, bg='yellow', width=400, height=400) 
canvas.create_line(0, 0, 400, 400)
canvas.create_rectangle(15, 15, 85, 85, fill='red')
canvas.create_oval(105, 105, 155, 155, fill='red')
canvas.pack()
# main loop
window.mainloop()