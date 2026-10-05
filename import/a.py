import pickle
from typing import Optional


class A:
    def __init__(self):
        self.a = 1
        self.b: Optional['B'] = None
    @classmethod
    def load(cls, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)


if __name__ == '__main__':
    a = A()
    a.save('a.pkl')