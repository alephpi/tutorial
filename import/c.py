from a import A

if __name__ == '__main__':
    a = A.load('a.pkl')
    print(a.a, a.b, a.b.b)