from anytree import Node, RenderTree
from anytree.exporter import DotExporter
n = int(input())
a, b = map(int, input().split())
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    root = Node(x)
    
