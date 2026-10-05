class B:
    def __init__(self):
        self.b = 2

from a import A


def main():
    a = A.load('a.pkl')
    a.b = B()
    a.save('a.pkl')

if __name__ == '__main__':
    main()