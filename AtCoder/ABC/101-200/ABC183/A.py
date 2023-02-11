def readinput():
    x=int(input())
    return x

def main(x):
    if x < 0:
        return 0
    else:
        return x

if __name__=='__main__':
    x=readinput()
    ans=main(x)
    print(ans)
