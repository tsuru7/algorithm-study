import sys
sys.setrecursionlimit(10**6)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))
DEBUG = False
def printd(*args):
    if DEBUG:
        print(*args)

def readinput():
    n,m=m_input()
    pillers = []
    heights = []
    for _ in range(m):
        k = i_input()
        heights.append(k-1)
        l = l_input()
        pillers.append(l)
    return n,m,heights,pillers

def main(n,m,heights,pillers):

    # initialize

    two = dict()
    one = dict()
    for i in range(m):
        if len(pillers[i]) > 0:
            color = pillers[i][heights[i]]
            if color not in one.keys():
                one[color] = [i]
            else:
                two[color] = one[color]
                two[color].append(i)
                del one[color]
    
    # print(f'pillers: {pillers}')
    # print(f'heights: {heights}')

    count = 0
    while len(two) > 0:
        # print(f'two: {two}')
        # print(f'heights: {heights}')
        two_next = dict()
        for color, places in two.items():
            p1, p2 = places
            heights[p1] -= 1
            heights[p2] -= 1
            for p in [p1, p2]:
                # print(f'p: {p}')
                if heights[p] >= 0:
                    color1 = pillers[p][heights[p]]
                    if color1 not in one.keys():
                        one[color1] = [p]
                    else:
                        two_next[color1] = one[color1]
                        two_next[color1].append(p)
                        del one[color1]
            count += 1
        two = two_next

    if count == n:
        return 'Yes'
    else:
        return 'No'

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,m,heights,pillers=readinput()
    ans=main(n,m,heights,pillers)
    printans(ans)
