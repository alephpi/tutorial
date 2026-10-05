class A:
    def __init__(self):
        print(__name__)
        print(__file__)

if __name__ == '__main__':
    a = A()