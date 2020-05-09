from collections import deque

def readinput():
    n = int(input())
    commands = []
    for i in range(n):
        command = input().split()
        commands.append(command)
    return n,commands

def main(n,commands):
    l = deque([])
    for i in range(n):
        command = commands[i]
        if (command[0]=='insert'):
            op = command[1]
            l.appendleft(op)
        elif(command[0]=='delete'):
            op = command[1]
            try:
                l.remove(op)
            except:
                pass
        elif(command[0]=='deleteFirst'):
            l.popleft()
        elif(command[0]=='deleteLast'):
            l.pop()
        else:
            pass
        #print(' '.join(l))

    return l
    
def main2():
    n = int(input())
    l = deque([])
    for i in range(n):
        command = input().split()
        if (command[0]=='insert'):
            op = command[1]
            l.appendleft(op)
        elif(command[0]=='delete'):
            op = command[1]
            try:
                l.remove(op)
            except:
                pass
        elif(command[0]=='deleteFirst'):
            l.popleft()
        elif(command[0]=='deleteLast'):
            l.pop()
        else:
            pass
        #print(' '.join(l))

    return l
if __name__=='__main__':
    #n, commands=readinput()
    #ans = main(n,commands)
    ans = main2()
    print(' '.join(ans))
