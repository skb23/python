class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_help(self.root,new_val)
    
    def insert_help(self,current,new):
        if(new>current.value):
            if current.right:
                self.insert_help(current.right,new)
            else:
                current.right=Node(new)
        else:
            if current.left:
                self.insert_help(current.left,new)
            else:
                current.left=Node(new)
                
    def search(self, find_val):
        return self.search_help(self.root,find_val)
        
    
    def search_help(self,start,find):
        #print"In finder " +str(start.value)
        if start:
            if(start.value==find):
                #print"Value matches"
                return True
            if(find>start.value):
                if(start.right):
                    if(start.right.value==find):
                        return True
                    else:
                        self.search_help(start.right,find)
            else:
                if(start.left):
                    if(start.left.value==find):
                        return True
                    else:
                        self.search_help(start.left,find)
        return False
    
     def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
