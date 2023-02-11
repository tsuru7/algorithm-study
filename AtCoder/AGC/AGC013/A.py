def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    a=l_input()
    return n,a

def get_seq(a, idx):
    if len(a) == idx + 1:
        return len(a)
    idx1 = 0
    for i in range(idx+1, len(a)):
        if a[i-1] <= a[i]:
            continue
        else:
            idx1 = i
            break
    else:
        idx1 = i + 1
    idx2 = 0
    for i in range(idx + 1, len(a)):
        if a[i-1] >= a[i]:
            continue
        else:
            idx2 = i
            break
    else:
        idx2 = i + 1
    return max(idx1, idx2)


def main(n,a):
    temp = get_seq(a, 0)
    count = 1
    # print(temp)
    while temp < len(a):
        temp = get_seq(a, temp)
        count += 1
        # print(temp)
    return count


def printans(ans):
    print(ans)

if __name__=='__main__':
    n,a=readinput()
    ans=main(n,a)
    printans(ans)
