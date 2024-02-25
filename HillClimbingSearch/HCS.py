import queue

dicPoint = {}
graph = {}
def readData():
    with open('input.txt', 'r') as file:
        ck = True
        for line in file:
            if line == "\n":
                ck=False
                continue
            if ck: #doc input1
                pair = line.strip().split(':')
                dicPoint[pair[0]] = int(pair[1])
            else: #doc input2
                if line[0] not in graph: graph[line[0]] = []
                n = len(line)
                for i in range(2, n, 2):
                    graph[line[0]].append(line[i])

    print("------------------------------------")
    print(dicPoint)
    for k, v in graph.items():
        print(f"{k}: {', '.join(v)}")

def HCS(s, f):
    with open("output.txt", "w") as output_file:
        output_file.write("{:<10} | {:<25} | {:<25} | {:<25}\n".format("PTTT", "TT Ke", "L1", "L"))
        output_file.write("-" * 85 + '\n')

        st = queue.LifoQueue() # stack chua cac dinh va nuoc di sau
        st.put(((s, dicPoint[s]), (0, [s])))
        q = queue.PriorityQueue() # priorityqueue chua cac dinh ke

        L = ""
        while not st.empty():
            x, i = st.get()

            tt, L1 = "", ""
            s1 = []

            if x[0] == f:
                res = "->".join(i[1])
                output_file.write("{:<10} | {:<25} | {:<25} | {:<25}\n".format(x[0], "TT", "", ""))
                output_file.write(f"{i[0]}: {res}\n")
                return

            if x[0] in graph:
                for c in graph[x[0]]:
                    tt = tt + c + ", "
                    q.put((-dicPoint[c], c))

            while not q.empty():
                v, k = q.get()
                s1.append(k)
                i1 = i[1] + [k]
                st.put(((k, dicPoint[k]), (i[0] + 1, i1)))

            for i in range(len(s1)-1, -1, -1): L1 = L1 + s1[i] + ", "

            #xoa cac ki tu thua, xoa 3 vi tri dau trong L vi da lay ra
            tt = tt.rstrip(", ")
            L1 = L1.rstrip(", ")
            L = L[3:] #cắt chuỗi đỉnh đầu được lấy
            if L1: L = L1 + ", " + L if L else L1
            output_file.write("{:<10} | {:<25} | {:<25} | {:<25}\n".format(x[0], tt, L1, L))

if __name__ == '__main__':
    readData()
    HCS('A', 'B')