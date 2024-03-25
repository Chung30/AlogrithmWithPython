from EEuclid import extendEuclid


class Module:
    @staticmethod
    def eulerPrime(n):
        # Sàng số nguyên tố nhanh
        d = {}
        # Xử lý các trường hợp đặc biệt của số 2
        while n % 2 == 0:
            if 2 not in d: d[2] = 1
            else: d[2]+=1
            n //= 2

        # Tìm các thừa số nguyên tố khác
        i = 3
        while i * i <= n:
            while n % i == 0:
                if i not in d: d[i] = 1
                n //= i
            i += 2

        # Nếu số n còn lại là một số nguyên tố lớn hơn 2
        if n > 2:
            if n not in d: d[n]=1
            else: d[n]+=1
        res = 1
        for k,v in d.items():
            res *= (k**v - k**(v-1))
        return d, res

    @staticmethod
    def calEuler(a, m, n):
        d = Module.eulerPrime(n)
        return ((a % n) ** (m % d[1])) % n
    @staticmethod
    def ModulChina(a, m, n):
        d = Module.eulerPrime(n)
        res = 0
        for k,v in d[0].items():
            tem=n/k
            ee = extendEuclid(tem, k)
            mod = ee.EEuclid(tem, k)[1]
            print(mod)
            res += mod * k * v * Module.calEuler(a, m, tem)
        return res

if __name__ == '__main__':
    print(Module.eulerPrime(63307))
    print(Module.ModulChina(241, 59, 63307))