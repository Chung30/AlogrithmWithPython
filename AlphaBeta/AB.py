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
            return val
        a = max(a, val)
    return val


def MinVal(u, a, b):
    if not u.children:
        return int(u.v)
    val = math.inf
    for node in u.children:
        val = min(val, MaxVal(node, a, b))
        if val <= a:
            return val
        b = min(b, val)
    return val


def Result(root):
    a = -math.inf
    b = math.inf
    max_value = -math.inf
    for node in root.children:
        value = MinVal(node, a, b)
        if value > max_value:
            max_value = value
    return max_value


if __name__ == '__main__':
    M, root = readData()
    print_tree(root)
    print(Result(root))
