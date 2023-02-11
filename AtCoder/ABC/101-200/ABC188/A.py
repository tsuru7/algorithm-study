def readinput():
    x,y=map(int,input().split())
    return x,y

def main(x,y):
    if x > y:
        if x - y < 3:
            return 'Yes'
        else:
            return 'No'
    else:
        if y - x < 3:
            return 'Yes'
        else:
            return 'No'

if __name__=='__main__':
    x,y=readinput()
    ans=main(x,y)
    print(ans)
