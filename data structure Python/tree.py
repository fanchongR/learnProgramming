################## list of lists

def binary_tree(r):
    return [r,[],[]]

def insert_left(root,new_branch):
    t = root.pop(1)
    if len(t)>1:
        root.insert(1,[new_branch,t,[]])
    else:
        root.insert(1,[new_branch,[],[]])
    return root        

def insert_right(root,new_branch):
    t = root.pop(2)
    if len(t)>1:
        root.insert(1,[new_branch,[],t])
    else:
        root.insert(1,[new_branch,[],[]])
    return root 



def get_root_val(root):
    return root[0]

def set_root_val(root,new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]


################## Nodes and References

class BinaryTree:
    def __init__(self,root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self,new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self,new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_root_val(self):
        return self.key
    def set_root_val(self,obj):
        self.key = obj

    def get_right_child(self):
        return self.right_child
    def get_left_child(self):
        return self.left_child


################################# binary heap  二叉堆 优先队列
#parent的key 小于等于child的key
#parent是p，child就是2p+1 2p
    
class BinHeap():
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
        
    def insert(self,k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)
    def perc_up(self,i):
        while i//2 > 0 and self.heap_list[i] < self.heap_list[i//2]:
            self.heap_list[i],self.heap_list[i//2] = self.heap_list[i//2],self.heap_list[i]
            i = i//2

    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val
    def perc_down(self,i):
        mc = self.min_child(i)
        while mc:
            if self.heap_list[mc] < self.heap_list[i]:         ###
                self.heap_list[mc],self.heap_list[i] = self.heap_list[i],self.heap_list[mc]
                i = mc
                mc = self.min_child(i)
    def min_child(self,i):
        if 2*i+1 <= self.current_size:
            if self.heap_list[2*i] > self.heap_list[2*i+1]:
                return 2*i+1
            else:
                return 2*i
        elif 2*i <= self.current_size:
            return 2*i
        else:
            return None
        
    def build_heap(self,a_list):
        i = len(a_list)//2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]        #
        while i > 0:
            self.perc_down(i)
            i -= 1
            
####################stack
class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
    
#################二叉树应用   有bug

def build_parse_tree(fp_exp):
    fp_list = fp_exp.split()
    e_tree = BinaryTree('')
    p_stack = Stack()
    p_stack.push(e_tree)
    currentnode = e_tree
    
    for i in range(fp_list):
        if i == '(':
            currentnode.insert_left('')
            p_stack.push(currentnode)
            currentnode = currentnode.get_left_child()
        if i not in ['(',')','+','-','*','/']:
            if currentnode.get_left_child() == None:
                currentnode.insert_left(i)
                p_stack.push(currentnode)
                currentnode = currentnode.get_left_child()
            else:
                currentnode.insert_right(i)
        if i in ['+','-','*','/']:
            currentnode = p_stack.pop()
            currentnode.set_root_val(i)
        if i == ')':
            currentnode = p_stack.pop()
            
                
            
            
def build_parse_tree(fp_exp):
    fp_list = fp_exp.split()
    p_stack = Stack()
    e_tree = BinaryTree(' ' )
    p_stack.push(e_tree)
    current_tree = e_tree
    for i in fp_list:
        if i == ' (' :
            current_tree.insert_left(' ' )
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in [ ' +' , ' -' , ' *' , ' /' , ' ) ' ]:
            current_tree.set_root_val(i)
            parent = p_stack.pop()
            current_tree = parent
        elif i in [ ' +' , ' -' , ' *' , ' /' ]:
            current_tree.set_root_val(i)
            current_tree.insert_right(' ' )
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ' ) ' :
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return e_tree
            
import operator
def evaluate(parse_tree):
    opers = { ' +' :operator.add, ' -' :operator.sub, ' *' :operator.mul,' /' :operator.truediv}
    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()
    if left and right:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left),evaluate(right))
    else:
        return parse_tree.get_root_val()

    
pt = build_parse_tree("((10+5)*3)")

############################################################################
################### 二叉树遍历

def preorder(tree):
    if tree != None:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

# 方法
def preorder(self):
    print(self.key)
    if self.left_child:
        self.left_child.preorder()
    if self.right_child != None:
        self.right_child.preorder()

        
def postorder(tree):
    if tree != None:
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())
        print(tree.get_root_val())

def inorder(tree):
    if tree != None:
        preorder(tree.get_left_child())
        print(tree.get_root_val())
        preorder(tree.get_right_child())
        



###############################################################################
###############################################################################
####################二叉搜索树

class TreeNode:
    def __init__(self,key,val,left = None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent
    def has_left_child(self):
        return self.left_child
    def has_right_child(self):
        return self.right_child
    def is_left_child(self):
        return self.parent and self.parent.left_child == self
    def is_right_child(self):
        return self.parent and self.parent.right_child == self
    def is_root(self):
        return not self.parent
    def is_leaf(self):
        return not (self.left_child or self.right_child)
    def has_any_children(self):
        return self.left_child or self.right_child
    def has_both_children(self):
        return self.left_child and self.right_child
    def replace_node_data(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def find_min(self):
        current_node = self
        while current_node.has_left_child():
            current_node = current_node.left_child
        return current_node
            
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def length(self):
        return self.size
    def __len__(self):                   # len()
        return self.size 

    def put(self,key,val):
        if self.root == None:
            self.root = TreeNode(key,val)
            self.size += 1
        else:
            self._put(key,val,self.root)
    def _put(self,key,val,current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key,val,current_node.left_child)
            else:
                current_node.left_child = TreeNode(key,val,parent=current_node)
                self.size += 1
        elif key > current_node.key:
            if current_node.has_right_child():
                self._put(key,val,current_node.right_child)
            else:
                current_node.right_child = TreeNode(key,val,parent=current_node)
                self.size += 1
        else:
            current_node.replace_node_data(key,val,current_node.left_child,current_node.right_child)
    def __setitem__(self,k,v):               # self['k']='v'
        self.put(k,v)
        
    def get(self,key):
        if self.root:
            ret = self._get(key,self.root)
            if ret:                             ###
                return ret.payload
            else:
                return None
        else:
            return None
    def _get(self,key,current_node):
        if key == current_node.key:
            return current_node
        elif key < current_node.key:
            if current_node.has_left_child():
                return self._get(key,current_node.left_child)
            else:
                return None
        else:
            if current_node.has_right_child():
                return self._get(key,current_node.right_child)
            else:
                return None
    def __getitem__(self,k):           # = self['k']
        return self.get(k)

    def __contains__(self,key):        #  if 'key' in self:
        if self.get(key):
            return True
        else:
            return False
            

    def delete(self,key):        
        if self.size > 1:
            node_to_move = self._get(key,self.root)
            if node_to_move:
                self.remove(node_to_move)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')
    def __delitem__(self,key):           # del instance[key] 
        self.delete(key)
        
            
    def remove(self,current_node):
        if current_node.is_leaf():
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
                
        elif current_node.has_any_children() and not current_node.has_both_children():    #
            if current_node.has_left_child():
                temp = current_node.left_child
            else:
                temp = current_node.right_child
            if current_node.is_root():
                current_node.replace_node_data(temp.key,temp.payload,temp.left_child,temp.right_child)
            elif current_node == current_node.parent.left_child:
                current_node.parent.left_child = temp
                temp.parent = current_node.parent
            else:
                current_node.parent.right_child = temp
                temp.parent = current_node.parent
                
        else:
            successor = current_node.right_child.find_min()
            self.remove(successor)
            current_node.key = successor.key
            current_node.payload = successor.payload



   # def __iter__(self):
    
            
                
                
                
            
                
            
            
            
        

