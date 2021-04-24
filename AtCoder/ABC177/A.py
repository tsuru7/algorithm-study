def readinput():
    d,t,s=map(int,input().split())
    return d,t,s

def main(d,t,s):
    if d<=t*s:
        return 'Yes'
    else:
        return 'No'

if __name__=='__main__':
    d,t,s=readinput()
    ans=main(d,t,s)
    print(ans)
