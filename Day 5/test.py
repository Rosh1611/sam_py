from tree_traversals import preorder,inorder,postorder
class BST:
    def __init__(self):
        self.key=None
        self.left_child=None
        self.right_child=None
    def iter_insert_node(self,root,element):
        if(not root.key):
            root.key=element
            return root
        cur=root
        prev=None
        while(self):
            prev=self
            if(element==cur.key):
                return root
            elif(element<cur.key):
                cur=cur.left_child
            else:
                cur=cur.right_child
        cur.key=element
        if(element<prev.key):
            prev.lchild=cur
        else:
            prev.rchild=cur
root_node=BST()
root_node.iter_insert_node(root_node,10)
root_node.iter_insert_node(root_node,20)
#root_node.iter_insert_node(root_node,15)
#root_node.iter_insert_node(root_node,5)



        
