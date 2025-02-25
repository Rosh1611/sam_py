from tree_traversals import preorder,inorder,postorder
class BST:
    def __init__(self,key=None):
        self.key=key
        self.left_child=None
        self.right_child=None
    def iter_insert_node(self,root,element):
        if(not root.key):
            root.key=element
            return root
        cur=root
        prev=None
        while(cur):
            prev=cur
            if(element==cur.key):
                return root
            elif(element<cur.key):
                cur=cur.left_child
            else:
                cur=cur.right_child
        cur=BST(element)
        if(element<prev.key):
            prev.left_child=cur
        else:
            prev.right_child=cur
        return root
root_node=BST()
root_node=root_node.iter_insert_node(root_node,10)
root_node=root_node.iter_insert_node(root_node,20)
root_node=root_node.iter_insert_node(root_node,15)
root_node=root_node.iter_insert_node(root_node,5)
inorder(root_node)
print()
preorder(root_node)
print()
postorder(root_node)
