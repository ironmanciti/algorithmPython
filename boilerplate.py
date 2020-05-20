import sys

def hello():
    print('Hello world to Python programming')

if __name__ == '__main__':
    hello()
    print(sys.argv)
    print(sys.argv[0])
    print(sys.argv[1])
