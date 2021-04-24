from math import pi
def readinput():
    r=int(input())
    return r

def main(r):
    return 2*pi*r

if __name__=='__main__':
    r=readinput()
    ans=main(r)
    print(ans)
