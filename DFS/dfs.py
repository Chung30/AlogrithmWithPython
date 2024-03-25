import queue

graph = {}
def readData():
    with open('input.txt', 'r') as file:
        for line in file:
            # print(line)
            if line[0] not in graph: graph[line[0]] = []
            n = len(line)
            for i in range(2, n, 2):
                graph[line[0]].append(line[i])

    print("------------------------------------")
    for k, v in graph.items():
        print(f"{k}: {', '.join(v)}")

def DFS(s, f):
    with open("output.txt", "w") as output_file:
        output_file.write("{:<10} | {:<25} | {:<25} | {:<25}\n".format("PTTT", "TT Ke", "Q", "L"))
        output_file.write("-" * 85 + '\n')

        st = queue.LifoQueue()
        st.put((s, [s]))
        d = {}
        d[s] = 0
        while not st.empty():
            tt, Q, L = '', '', ''
            x, v = st.get()
            print(x, v)
            if x == f:
                res = "->".join(v)
                output_file.write("{:<10} | {:<25} | {:<25} | {:<25}\n".format(x[0], "TT", "", ""))
                output_file.write(f"{d[x]}: {res}\n")
                return

            if x in graph:
                for c in graph[x]:
                    tt += ', ' + c
                    if c not in d:
                        st.put((c, v + [c]))
                        d[c] = d[x] + 1

                for c in d:
                    Q += ', ' + c

                st1 = list(st.queue)
                for c in st1:
                    L += ' ,' + c[0]

                output_file.write("{:<10} | {:<25} | {:<25} | {:<25}\n".format(x, tt[2:], Q[2:], L[2:]))

if __name__ == '__main__':
    readData()
    DFS('A', 'K')