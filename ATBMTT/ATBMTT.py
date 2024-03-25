from EEuclid import extendEuclid
from Modulo import Modul

if __name__ == '__main__':
    # mod = Modul(1024, 3, 7)
    # mod = Modul(239, 6653, 6653)
    # print(mod.calculate_modulo())

    mod = extendEuclid(7841, 1974)
    # mod = extendEuclid(19*71, 37)
    print(mod.modul())