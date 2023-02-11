def readinput():
    n=int(input())
    return n

def main(x):
    if 400<=x and x<=599:
        return 8
    elif 600<=x and x<=799:
        return 7
    elif 800<=x and x<=999:
        return 6
    elif 1000<=x and x<=1199:
        return 5
    elif 1200<=x and x<=1399:
        return 4
    elif 1400<=x and x<=1599:
        return 3
    elif 1600<=x and x<=1799:
        return 2
    elif 1800<=x and x<=1999:
        return 1
    else:
        return 0

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
