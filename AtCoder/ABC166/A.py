def readinput():
    s=input()
    return s

def main(s):
    if s=='ABC':
        return 'ARC'
    elif s=='ARC':
        return 'ABC'
    ans=''
    return ans

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
