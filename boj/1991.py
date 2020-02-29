from collections import defaultdict

class Node:
    def __init__(self, value):
        self.value = value

class mydefaultdict(defaultdict):
    def __missing__(self, key):
        self[key] = self.default_factory(key)
        return self[key]

n = int(input())
node_dict = mydefaultdict(Node)
for _ in range(n):
    node, left, right = input().split()
    node = node_dict[node]
    left = node_dict[left] if left != '.' else None
    right = node_dict[right] if right != '.' else None
    node.left = left
    node.right = right

# pre-order
def preorder(node):
    if node is None: return
    print(node.value, end='')
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if node is None: return
    inorder(node.left)
    print(node.value, end='')
    inorder(node.right)

def postorder(node):
    if node is None: return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end='')

preorder(node_dict['A'])
print()
inorder(node_dict['A'])
print()
postorder(node_dict['A'])
