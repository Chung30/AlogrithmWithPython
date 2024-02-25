class Modul:
    def __init__(self, a, m, n):
        self.a = a % n
        self.m = m
        self.n = n
        self.l = [self.a]
        self.m1 = bin(self.m)[2:]
        self.res = 1
    def calculate_modulo(self):
        for i in reversed(self.m1):
            x = self.l[-1]
            print(x)
            if i == '1':
                self.res = (self.res * x) % self.n
            self.l.append((x * x) % self.n)
        return self.res
