import math


class Node:
    def __init__(self, v):
        self.v = v
        self.children = []

    def __str__(self):
        return f"{self.v}"

def print_tree(node, level=0):
    print("  " * level + node.v)
    for child in node.children:
        print_tree(child, level + 1)

def readData():
    nodes = {}
    ck = True
    with open('input.txt', 'r') as file:
        for line in file:
            if ck == True:
                M = int(line[0])  # Đọc số đầu tiên
                root = line.strip().split()[1] # Đọc root
                if root not in nodes:
                    nodes[root] = Node(root)
                ck = False
            else:
                parent, child = line.strip().split(':')
                if parent not in nodes:
                    nodes[parent] = Node(parent)
                parent_node = nodes[parent]
                children_info = child.split(',')
                for info in children_info:
                    child_value = info.split(':')[0]
                    if child_value not in nodes:
                        nodes[child_value] = Node(child_value)
                    child_node = nodes[child_value]
                    parent_node.children.append(child_node)
        return M, nodes[root]

def MaxVal(u, a, b):
    if not u.children:
        return int(u.v)
    val = -math.inf
    for node in u.children:
        val = max(val, MinVal(node, a, b))
        if val >= b:
            print(val, a, b)
            print("cut")
            node.v = val
            return val
        a = max(a, val)
        print(val, a, b)
    u.v = val
    return val

def MinVal(u, a, b):
    if not u.children:
        return int(u.v)
    val = math.inf
    for node in u.children:
        val = min(val, MaxVal(node, a, b))
        if val <= a:
            print(val, a, b)
            print("cut")
            node.v = val
            return val
        b = min(b, val)
        print(val, a, b)
    u.v = val
    return val


def Result(root):
    a = -math.inf
    b = math.inf
    val = -math.inf
    val = MinVal(root, a, b)
    # for node in root.children:
    #     value = MinVal(node, a, b)
    #     if value > val:
    #         val = value
    #     node.v = val
    #     print(val, a, b)
    return val

def solve(node, file, level=0):
    file.write("  " * level + f"{node.v}" + "\n")
    for child in node.children:
        solve(child, file, level + 1)

def print_tree(root, filename):
    with open(filename, 'w') as file:
        solve(root, file)

if __name__ == '__main__':
    M, root = readData()
    # print_tree(root)
    print(Result(root))
    print_tree(root, 'output.txt')
