from queue import PriorityQueue, LifoQueue


class Node:
    def __init__(self, egde, weight) -> None:
        self.egde = egde
        self.weight = weight

    def __str__(self) -> str:
        return self.egde + " " + str(self.weight)


dicPoint = []
grap = {}


def readData():
    with open("input.txt", "r") as file:
        ck = True
        for line in file:
            if line == '\n':
                ck = False
                continue
            if ck:
                e, w = line.split(":")
                tmp = Node(e, int(w))
                dicPoint.append(tmp)
            else:
                if line[0] not in grap: grap[line[0]] = []
                n = len(line)
                for i in range(2, n, 2):
                    grap[line[0]].append(line[i])
    for i in dicPoint:
        print(str(i))
    print(grap)


def hill_climbing(graph, intial_state: Node, end_state: Node) -> str:
    st = LifoQueue()
    Q = PriorityQueue()
    st.put((intial_state, (0, [intial_state.egde])))

    L = ""
    while not st.empty():
        x, i = st.get()
        s = []
        tt, L1 = "", ""
        if x.egde == end_state.egde:
            res = "->".join(i[1])
            print(x.egde, "TT", "", "")
            print(f"{i[0]} : {res}\n")
            return
        for c in graph[x.egde]:
            tt = tt + c + ", "
            for node in dicPoint:
                if node.egde == c:
                    Q.put((-node.weight, node.egde))
                    break

        while not Q.empty():
            v, k = Q.get()
            s.append(k)
            i1 = i[1] + [k]
            tmp = Node(k, v)
            st.put((tmp, (i[0] + 1, i1)))
        for i in range(len(s) - 1, -1, -1):
            L1 = L1 + s[i] + ", "

        tt = tt.rstrip(", ")
        L1 = L1.rstrip(", ")
        L = L[3:]
        L = L1 + ", " + L if L else L1
        print(x.egde, tt, L1, L)


if __name__ == '__main__':
    readData()
    hill_climbing(grap, Node("A", 20), Node("B", 0))