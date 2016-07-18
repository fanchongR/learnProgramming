#####################递归 河汉塔

def move_tower(height,from_pole,to_pole,with_pole):
    if height > 1:
        move_tower(height-1,from_pole,with_pole,to_pole)
        move_disk(height,from_pole,to_pole)
        move_tower(height-1,with_pole,to_pole,from_pole)
    else:
        move_disk(height,from_pole,to_pole)

def move_disk(height,fp,tp):
    print("moving",height,"disk from",fp,"to",tp)


move_tower(5,'A','C','B')


#######################查找  是否要先排序？对于长的列表排序很耗资源，还不如顺序查找
#######Sequential Search  顺序查找   复杂度n
def sequential_search(a_list,item):
    for temp in a_list:
        if temp == item:return True
    return False

# 复杂度n
def ordered_sequential_search(a_list,item):
    for temp in a_list:
        if temp > item:return False
        if temp == item:return True
    return False

########The Binary Search    二进制搜索
def binary_search(a_list,item):
    first = 0
    last = len(a_list) - 1
    while first <= last:
        midpoint = int((first + last)/2)
        if a_list[midpoint] == item:return True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False

##################################数据结构 hashing



######################################sorting

def bubble_sort(a_list):
    for pass_num in range(1,len(a_list)):
        for i in range(len(a_list)-pass_num):
            if a_list[i] > a_list[i+1]:
                a_list[i],a_list[i+1] = a_list[i+1],a_list[i]
    return a_list

            
            
def short_bubble_sort(a_list):
    for pass_num in range(1,len(a_list)):
        exchange = False
        for i in range(len(a_list)-pass_num):
            if a_list[i] > a_list[i+1]:
                a_list[i],a_list[i+1] = a_list[i+1],a_list[i]
                exchange = True
        if not exchange: return a_list
    return a_list
        
###############

def selection_sort(a_list):
    N = len(a_list)
    for pass_num in range(1,N):
        maxlocation = 0
        for i in range(N-pass_num):
            if a_list[maxlocation] < a_list[i+1]:
                maxlocation = i+1
        a_list[maxlocation],a_list[N-pass_num] = a_list[N-pass_num],a_list[maxlocation]
    return a_list

###############

def insertion_sort(a_list):
    for pass_num in range(1,len(a_list)):
        valuenow = a_list[pass_num]
        index = pass_num - 1
        while index > -1 and valuenow < a_list[index]:
            a_list[index+1] = a_list[index]
            index -= 1
        a_list[index+1] = valuenow
    return a_list


##############

def gap_insertion_sort(a_list,start,gap):
    end = start + gap
    while end < len(a_list):
        index = end - gap
        valuenow = a_list[end]
        while index > start - 1 and valuenow < a_list[index]:
            a_list[index+gap] = a_list[index]
            index -= gap
        a_list[index+gap] = valuenow
        end += gap
    

def shell_sort(a_list):
    gap = len(a_list)//2
    while gap > 0:
        for start in range(gap):
            gap_insertion_sort(a_list,start,gap)
        gap = gap//2
    

#####################

def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list)//2
        left = a_list[:mid]
        right = a_list[mid:]
        merge_sort(left)
        merge_sort(right)

        i = 0 ; j = 0 ; k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a_list[k] = left[i]
                i += 1
            else:
                a_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            a_list[k] = left[i]
            i +=1 ; k +=1
        while j < len(right):
            a_list[k] = right[j]
            j +=1 ; k +=1
    




#########################

def bubble(a):
    N = len(a)
    for passnum in range(1,N)[::-1]:
        for i in range(passnum):
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
    return a


def insertsort(a):
    N = len(a)
    for passnum in range(1,N):
        i = passnum - 1
        valuenow = a[passnum]
        while a[i] > valuenow and i > -1:
            a[i+1] = a[i]
            i -= 1
        a[i+1] = valuenow
    return a

def selectsort(a):
    N = len(a)
    for passnum in range(1,N)[::-1]:
        maxnum = a[passnum]
        maxindex = passnum
        for i in range(0,passnum):
            if a[i] > maxnum:
                maxnum = a[i]
                maxindex = i
        a[maxindex],a[passnum] = a[passnum],a[maxindex]
    return a

def mergesort(a):
    N = len(a)
    if N < 2:
        return a

    midpoint = N//2
    left = a[:midpoint]
    right = a[midpoint:]
    mergesort(left)
    mergesort(right)  

    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
            k += 1
        else:
            a[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        a[k] = left[i]
        i += 1; k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1; k += 1
    
            
    
#########################quick sort
#写helper函数，因为这样可以传递index之类的参数，而不用切片

def quicksort(a):
    quicksort_helper(a,0,len(a)-1)
    return a
    
def quicksort_helper(a,start,end):
    i = start
    j = end
    if j <= i or j > len(a)-1:
        return a
    
    point = a[start]
    while i < j :
        while a[i] <= point and i < j:
            i += 1
        while a[j] >= point and i <= j:
            j -= 1
        if i < j:
            a[i],a[j] = a[j],a[i]
    a[start],a[j] = a[j],a[start]
    quicksort_helper(a,start,j-1)
    quicksort_helper(a,j+1,end)

quicksort([4,5,2,1,3,6,6,8,9,9,0,0,0,3,1,4,5,7])
a = [4,5,2,1,3,6,6,8,9,9,0,0,0,3,1,4,5,7]
[0, 0, 0, 1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9]


####################quicksort 2
def quicksort2(a):
    quicksort2_helper(a,0,len(a)-1)
    return a

def quicksort2_helper(a,start,end):
    if start >= end:
        return a
    
    point = a[start]
    i = start ; j = i + 1 ; k = end;
    while j<=k :
        if a[j] < point:
            a[i],a[j] = a[j],a[i]
            i += 1
            j += 1
        elif a[j] > point:
            a[j],a[k] = a[k],a[j]
            k -= 1
        else:
            j += 1

    quicksort2_helper(a,start,i-1)
    quicksort2_helper(a,j,end)




        
    
    
            
       
            
        
        

        
             
    







    

