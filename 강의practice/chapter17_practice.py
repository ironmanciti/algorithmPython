with open('test.txt', "w") as file3:
    data = file3.write("한국소프트웨어 산업협회 훈련과정 :\n 알고리즘으로 배우는 Python")

try:
    f = open('test.txt', 'r')
    text = f.read()
    print(text)
    f.close()
except IOError:
    sys.write("File reading error")
