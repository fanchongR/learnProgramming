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

def par_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():return False
            s.pop()
    if s.is_empty():
        return True
    else:
        return False

#匹配多个平衡符号
def match(open,close):
    opens = '({['
    closes = ')}]'
    return opens.index(open) == closes.index(close)

def par_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol in '({[':
            s.push(symbol)
        else:
            if s.is_empty():return False
            if match(s.peek(),symbol):
                s.pop()
            else:
                return False
    if s.is_empty():
        return True
    else:
        return False

######################################queue

class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    
def hot_potato(name_list,num):
    sim_queue=Queue()
    for name in name_list:
        sim_queue.enqueue(name)
    while sim_queue.size()>1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()


######################################deque
class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self,item):
        self.items.append(item)

    def add_rear(self,item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)



def pal_checker(a_string):
    char_deque = Deque()
    for ch in a_string:
        char_deque.add_front(ch)
    while char_deque.size()>1:
        ch1 = char_deque.remove_front()
        ch2 = char_deque.remove_rear()
        if ch1 != ch2: return False
    return True

######################################linked list
class Node:
    def __init__(self,init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self,new_data):
        self.data = new_data
            
    def set_next(self,new_next):
        self.next = new_next

class UnorderedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def add(self,item):               #每加一个node节点，都放在最前面，也就是head
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            current = current.get_next()
            count +=1
        return count

    def search(self,item):
        current = self.head
        while current != None:
            if current.get_data() == item:return True
            current = current.get_next()
        return False

    def remove(self,item):
        current = self.head
        previous = None
        while current != None:
            if current.get_data() == item:
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
                break
            else:
                previous = current
                current = current.get_next()
        
            
mylist = UnorderedList()

######################################Ordered List
class OrderedList():
    def __init__(self):
        self.head = None
        
        

