def readinput():
    a,b=map(int,input().split())
    return a,b

def main(a,b):
    for i in range(20000):
        if i*108//100 - i ==a and i*110//100 - i ==b:
            return i
    return -1

if __name__=='__main__':
    a,b=readinput()
    ans=main(a,b)
    print(ans)
