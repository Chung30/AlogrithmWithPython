import queue

dicPoint = {}
graph = {}

def readData():
    with open('input.txt', 'r') as file:
        ck = True
        for line in file:
            if line == "\n":
                ck = False
                continue
            if ck:  # Đọc input1
                pair = line.strip().split(':')
                dicPoint[pair[0]] = int(pair[1])
            else:  # Đọc input2
                # tách dần dần từ đỉnh gốc xuống các đỉnh lá VD: A:B-10,C-7,D-13,E-19
                # tách A trước bằng dấu :
                # tách dần các đỉnh ở lá và đường đi bằng dấu ,
                # tách dần đỉnh lá và trọng số đường đi bằng dấu -
                # tất cả lưu trong map(dictionary) graph
                point, nodes = line.split(':') #{đỉnh} và {các đỉnh kề cùng trọng số đường đi}
                graph[point] = []
                listNodes = nodes.strip().split(',')
                for node in listNodes:
                    target, weight = node.split('-')
                    graph[point].append((target, int(weight)))

    print("------------------------------------")
    print(dicPoint)
    for k, v in graph.items():
        print(f"{k}: {', '.join([f'{target}-{weight}' for target, weight in v])}")

def Astar(s, f):
    with open("output.txt", "w", encoding="utf-8") as output_file:
        output_file.write("{:<5} | {:<5} | {:<5} | {:<5} | {:<5} | {:<5} | {:<5}\n".
                          format("PTTT", "TT Ke", "k(u,v)", "g(u)", "h(u)", "f(u)", "L"))

        L = queue.PriorityQueue()  # gồm f, đỉnh kề, g, list chứa đường đi
        L.put((dicPoint[s], s, 0, [(0, s)], [s]))  # Đặt giá trị ban đầu vào hàng đợi để L sắp xếp theo f

        while not L.empty():
            output_file.write("-" * 70 + '\n')
            resultString = ""
            fu, p, g, l1, l = L.get()  # Lấy giá trị từ hàng đợi
            l1.pop(0)
            if p == f:
                print(l, fu)
                res = "->".join(l) + " với độ dài là: " + f"{fu}"
                resultString = resultString + "{:<5} | {:<5} \n".format(p, "TTKT")
                resultString = resultString + res
                output_file.write(resultString + "\n")
                return
            if p in graph:
                ck = True
                lString1 = [] # chứa chuỗi theo từng dòng
                for v, w in graph[p]:
                    lString = ""
                    gv = g + w
                    fv = gv + dicPoint[v]
                    l1.append((fv, v))
                    l1.sort()
                    for lw, lv in l1:
                        lString = lString + lv + "-" + str(lw) + ","
                    if ck == True:
                        lString1.append("{:<5} | {:<5} | {:<6} | {:<5} | {:<5} | {:<5} | ".
                                          format(p, v, w, gv, dicPoint[v], fv))
                        ck = False
                    else:
                        lString1.append("{:<5} | {:<5} | {:<6} | {:<5} | {:<5} | {:<5} | ".
                                       format("", v, w, gv, dicPoint[v], fv))
                    L.put((fv, v, gv, l1, l + [v]))  # Đặt tuple mới với fu là giá trị để sắp xếp

                #  tách lString
                lString2 = []
                lString = lString[:-1]
                while len(lString) > 20:
                    lString2.append(lString[:20])
                    lString = lString[20:]
                if lString:
                    lString2.append(lString)

                #  Ghép vào bảng:
                for i in range(max(len(lString1), len(lString2))):
                    # Lấy chuỗi từ lOutput hoặc để chuỗi rỗng nếu lOutput đã hết
                    chunk1 = lString1[i] if i < len(lString1) else "      |       |        |       |       |       | "
                    # Lấy chuỗi từ sublString hoặc để chuỗi rỗng nếu sublString đã hết
                    chunk2 = lString2[i] if i < len(lString2) else ''
                    resultString = resultString + chunk1 + chunk2 + '\n'
                output_file.write(resultString)

if __name__ == "__main__":
    readData()
    Astar('A', 'I')
