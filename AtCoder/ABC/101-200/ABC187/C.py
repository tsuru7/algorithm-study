from bisect import bisect_left

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

def readinput():
    n=int(input())
    s0List = []
    s1List = []
    for _ in range(n):
        s = input()
        if s[0] == '!':
            s1List.append(s[1:])
        else:
            s0List.append(s)
    return n,s0List, s1List

def main(n, s0List, s1List):
    s0List.sort()
    s1List.sort()
    for s in s0List:
        if index(s1List, s) != -1:
            return s
    else:
        return 'satisfiable'

if __name__=='__main__':
    n,s0List, s1List=readinput()
    ans=main(n,s0List, s1List)
    print(ans)
