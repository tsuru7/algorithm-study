from itertools import permutations

def readinput():
    n,k=map(int,input().split())
    table = []
    for _ in range(n):
        table.append(list(map(int,input().split())))
    return n,k,table

def main(n,k,table):
    a = [x for x in range(1, n)]
    count=0
    for p in permutations(a,n-1):
        # print(p)
        t = 0
        src=0
        for dst in p:
            # print(t, table[src][dst])
            t += table[src][dst]
            src=dst
        # print(t, table[dst][0])
        t += table[dst][0]
        # print(t)
        if t == k:
            count += 1
    return count

if __name__=='__main__':
    n,k,table=readinput()
    ans=main(n,k,table)
    print(ans)
