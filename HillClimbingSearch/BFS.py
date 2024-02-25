import queue

dicPoint = {}
graph = {}
class ReadData:
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

def BestFirstSeach(s, f):
    with open("output.txt", "w") as output_file:
        output_file.write("{:<10} | {:<25} | {:<25}\n".format("PTTT", "TT Ke", "L"))
        output_file.write("-" * 65 + '\n')

        pq = queue.PriorityQueue()
        #pq chua cap dinh va trong so (trong so de sap xep), cap mang [] chua cac nuoc di va so buoc di
        pq.put(((dicPoint[s], s), ([s], 0)))

        L = ""
        while not pq.empty():
            a = [] #mang chua dinh ke
            K = ""
            x,i = pq.get()
            if x[1] == f:
                output_file.write("{:<10} | {:<25} | {:<25}\n".format(x[1], "TT", ""))
                output_file.write(f"{i[1]}: {i[0]}")
                return
            if x[1] in graph:
                for c in graph[x[1]]:
                    a = a + [c]
                    v=i[0]+[c]
                    pq.put(((dicPoint[c], c),(v,i[1]+1)))
            K = ', '.join([f"{k}" for k in a])
            pq_ = list(pq.queue)
            L = ', '.join([f"{i[0][1]}" for i in pq_])
            output_file.write("{:<10} | {:<25} | {:<25}\n".format(x[1], K, L))

if __name__ == '__main__':
    ReadData()
    BestFirstSeach('A', 'B')