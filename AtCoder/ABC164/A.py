def readinput():
    s,w=map(int,input().split())
    return s,w

def main(s,w):
    if w>=s:
        return 'unsafe'
    else:
        return 'safe'

if __name__=='__main__':
    s,w=readinput()
    ans=main(s,w)
    print(ans)
