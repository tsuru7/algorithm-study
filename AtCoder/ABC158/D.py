def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    s = input()
    q = i_input()
    query = []
    for _ in range(q):
        tmp = input().split()
        if tmp[0] == '1':
            query.append([1])
        else:
            query.append([2, int(tmp[1]), tmp[2]])
    return s, q, query

def main(s, q, query):
    reverse = 0
    left = []
    right = []
    for q in query:
        if q[0] == 1:
            reverse = (reverse + 1) % 2
        else:
            f = q[1]
            c = q[2]
            if (reverse == 0 and f == 1) or (reverse == 1 and f == 2):
                left.append(c)
            else:
                right.append(c)
    if reverse == 0:
        return ''.join(left[::-1]) + s + ''.join(right)
    else:
        return ''.join(right[::-1]) + s[::-1] + ''.join(left)

def printans(ans):
    print(ans)

if __name__=='__main__':
    s, q, query=readinput()
    ans=main(s, q, query)
    printans(ans)
