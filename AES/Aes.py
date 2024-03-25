from constants import *

class aes:
    def __init__(self, plainText, cipherKey, n):
        self.n = n
        self.mPlain = self.AddToMatrix(plainText)
        self.mKey = self.AddToMatrix(cipherKey)

    def AddToMatrix(self, str):
        matrix = [[None] * self.n for _ in range(self.n)]
        index = 0
        for i in range(0, len(str), 2):
            row = index % self.n
            col = index // self.n
            matrix[row][col] = str[i:i+2]
            index += 1
        return matrix

    def printMatrix(self, matrix):
        for row in matrix:
            for v in row:
                print(v, end=' ')
            print()

    def subBytes(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                v = matrix[i][j]
                row = int(v[0], 16)
                col = int(v[1], 16)
                matrix[i][j] = S_Box[row][col]
        # self.printMatrix(matrix)
        return matrix

    def shiftRows(self, matrix):
        for i in range(self.n):
            matrix[i] = self.rotateRow(matrix[i], i)
        # self.printMatrix(matrix)
        return matrix

    def rotateRow(self, row, n):
        return row[n:] + row[:n]

    def mixColumns(self, matrix):
        mixMatrix = [[0] * self.n for _ in range(self.n)]
        for row in range(self.n):
            for col in range(self.n):
                mixMatrix[row][col] = self.resMix(matrix, row, col)
        # self.printMatrix(mixMatrix)
        return mixMatrix

    def resMix(self, matrix, row, col):
        res = 0
        for i in range(self.n):
            mbin = bin(int(matrix[i][col], 16))[2:].zfill(8)
            # print(matrix[i][col] + " " + mbin + " " + mbin[0] + " " + (mbin[1:] + '0'))
            if M_Mix[row][i] == '02':
                if mbin[0] == '0':
                    res ^= int(mbin[1:] + '0', 2)
                else:
                    res ^= int(mbin[1:] + '0', 2) ^ int('1b', 16)
            elif M_Mix[row][i] == '03':
                res ^= int(matrix[i][col], 16)
                if mbin[0] == '0':
                    res ^= int(mbin[1:] + '0', 2)
                else:
                    res ^= int(mbin[1:] + '0', 2) ^ int('1b', 16)
            else:
                res ^= int(matrix[i][col], 16)
        return hex(res)[2:].zfill(2)

    def AxorB(self, a, b):
        return hex(int(a, 16) ^ int(b, 16))[2:].zfill(2)


    def addRoundKey(self, matrix):
        for row in range(self.n):
            for col in range(self.n):
                matrix[row][col] = self.AxorB(matrix[row][col], self.mKey[row][col])
        return matrix

    def createKey(self, index):
        temp = [self.mKey[i][0] for i in range(self.n)]
        w0 = [self.mKey[i][self.n - 1] for i in range(self.n)]
        w0 = self.rotateRow(w0, 1)
        w0 = self.subWord(w0)
        w0[0] = self.AxorB(w0[0], RC[index])

        for i in range(self.n):
            self.mKey[i][0] = self.AxorB(w0[i], temp[i])
        for col in range(1, self.n):
            for i in range(self.n):
                self.mKey[i][col] = self.AxorB(self.mKey[i][col], self.mKey[i][col - 1])
        print(self.mKey)

    def subWord(self, matrix):
        for i in range(self.n):
            v = matrix[i]
            row = int(v[0], 16)
            col = int(v[1], 16)
            matrix[i] = S_Box[row][col]
        return matrix

    def solve(self, matrix):
        res = self.addRoundKey(self.mPlain)

        for i in range(1, 11):
            print(i)
            print(res)
            res = self.subBytes(res)
            print(res)
            res = self.shiftRows(res)
            print(res)
            if i != 10:
                res = self.mixColumns(res)
                print(res)
            self.createKey(i-1)
            res = self.addRoundKey(res)

        return res

if __name__ == '__main__':
    plain = '3243f6a8885a308d313198a2e0370734'
    # plain = '193de3bea0f4e22b9ac68d2ae9f84808'
    key = '2b7e151628aed2a6abf7158809cf4f3c'
    a = aes(plain, key, 4)
    print(a.mPlain)
    print(a.mKey)
    print("start")
    print(a.solve(a.mPlain))