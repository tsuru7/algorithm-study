def maxHeapify(a, i):
    #print('maxHeapify(a,{})'.format(i))
    #print(' '.join(map(str,a)))
    h=len(a)-1
    l=2*i
    r=2*i+1
    if l<=h and a[l]>a[i]:
        largest=l
    else:
        largest=i
    if r<=h and a[r]>a[largest]:
        largest=r
    if largest!=i:
        a[largest],a[i]=a[i],a[largest]
        maxHeapify(a,largest)

def buildMaxHeap(a):
    h=len(a)-1
    for i in range(h//2, 0, -1):
        maxHeapify(a, i)   

def insert(a, op):
    a.append(op)
    buildMaxHeap(a)

def heapIncreaseKey(a,i,key):
    h=len(a)-1
    if key<a[i]:
        raise Exception
    a[i]=key
    parent=i//2
    current=i
    while (current > 1) and (a[parent] < a[current]):
        a[parent],a[current]=a[current],a[parent]
        current=parent
        parent=current//2


def insert2(a,op):
    a.append(-1)
    h=len(a)-1
    heapIncreaseKey(a,h,op)

def extract(a):
    h=len(a)-1
    next=3
    while(next<=h):
        p=next//2
        a[p]=a[next]
        next=2*next+1
    if next-1==h:
        a[h//2]=a[h]
    a.pop()
    buildMaxHeap(a)

def extract2(a):
    h=len(a)-1
    a.pop(1)
    buildMaxHeap(a)

def extract3(a):
    ah=a.pop()
    a[1]=ah
    maxHeapify(a,1)

a=[-1]
s=input()
while(s != 'end'):
    cmds=s.split()
    if(cmds[0]=='insert'):
        op=int(cmds[1])
        insert2(a, op)
    elif(cmds[0]=='extract'):
        print(a[1])
        extract3(a)
    s=input()
