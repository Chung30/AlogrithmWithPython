class extendEuclid:
    def __init__(self, a, n):
        self.a = a
        self.n = n
    def EEuclid(self, a, b):
        if a == 0:
            return 1, 0, b
        else:
            x, y, gcd = self.EEuclid(b % a, a)
            print(x,y,gcd)
            return y, x - (b // a) * y, gcd
    def modul(self):
        x, y, gcd = self.EEuclid(self.a, self.n)
        if gcd != 1:
            return "No cmt"
        else:
            return y
