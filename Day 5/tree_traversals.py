def preorder(root):
    if(root):
        print(root.key,end=" ")
        preorder(root.left_child)
        preorder(root.right_child)

def inorder(root):
    if(root):
        inorder(root.left_child)
        print(root.key,end=" ")
        inorder(root.right_child)

def postorder(root):
    if(root):
        postorder(root.left_child)
        postorder(root.right_child)
        print(root.key,end=" ")