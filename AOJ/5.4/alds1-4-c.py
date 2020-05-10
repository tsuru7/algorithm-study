def readinput():
    n=int(input())
    commands = []
    for i in range(n):
        command=input().split()
        commands.append(command)
    return n, commands

def main(n,commands):
    d = dict()
    for cmd in commands:
        if(cmd[0]=='insert'):
            d[cmd[1]]=cmd[1]
        elif(cmd[0]=='find'):
            if(cmd[1] in d):
                print('yes')
            else:
                print('no')

if __name__=='__main__':
    n,commands=readinput()
    main(n,commands)
