import heapq

def insert(a,key):
    key2=-key
    heapq.heappush(a,key2)

def extract(a):
    key=heapq.heappop(a)
    return -key

a=[]
cmds=input().split()
while(cmds[0] != 'end'):
    if(cmds[0]=='insert'):
        op=int(cmds[1])
        insert(a,op)
    elif(cmds[0]=='extract'):
        print(extract(a))
    cmds=input().split()

