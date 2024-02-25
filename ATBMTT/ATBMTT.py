from EEuclid import extendEuclid
from Modulo import Modul

if __name__ == '__main__':
    mod = Modul(1024, 3, 7)
    # mod = Modul(239, 6653, 6653)
    print(mod.calculate_modulo())

    # mod = extendEuclid(1974, 7841)
    # mod = extendEuclid(37*19, 71)
    # print(mod.modul())