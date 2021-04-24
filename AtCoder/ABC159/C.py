def readinput():
    l=int(input())
    return l

def main(l):
    ans=(l/3)**3
    return ans

if __name__=='__main__':
    l=readinput()
    ans=main(l)
    print(ans)
