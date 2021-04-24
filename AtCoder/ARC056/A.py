def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    a,b,k,l=m_input()
    return a,b,k,l

def main(a,b,k,l):
    cost1 = ( k // l ) * b + ( k % l ) * a
    cost2 = ((k // l)+1) * b
    return min(cost1, cost2)

def printans(ans):
    print(ans)

if __name__=='__main__':
    a,b,k,l=readinput()
    ans=main(a,b,k,l)
    printans(ans)
