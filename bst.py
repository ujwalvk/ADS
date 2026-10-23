class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,data):
    if root is None:
        return Node(data)
    if data<root.data:
        root.left = insert(root.left,data)
    elif data>root.data:
        root.right=insert(root.right,data)
    return root
def search(root,key):
    if root is None or key==root.data:
        return root
    if key<root.data:
        return search(root.left,key)
    else:
        return search(root.right,key)
    

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
def preorder(root):
    if root is not None:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")
def min_val(root):
    current=root
    while current.left is not None:
        current =current.left
    return current

def delete(root,key):
    if root is None:
        return None
    if key<root.data:
        root.left=delete(root.left,key)
    elif key>root.data:
        root.right=delete(root.right,key)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            succesor=min_val(root.right)
            root.data=succesor.data
            root.right=delete(root.right,succesor.data)
    return root


            



# def print_tree(root,level=0,prefix="Root:"):
#     if root is not None:
#         print(" "*(level*3),prefix+str(root.data))
#         print_tree(root.left,level+1,"L--")
#         print_tree(root.right,level+1,"R--")

root=None
val=[12,34,52,1,4,56]

for i in val:
    root=insert(root,i)
# print_tree(root)

print("inorder")
inorder(root)
print('\npostorder')
postorder(root)
print('\npreorder')
preorder(root)

key = 4
result = search(root, key)

if result is not None:
    print("\nElement found:", key)
else:
    print("\nElement not found:", key)
delete(root,1)
inorder(root)
