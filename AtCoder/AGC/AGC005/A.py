from collections import deque

def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    x = input()
    return x

def main(x):
    stack = deque()
    for c in x:
        if c == 'T' and len(stack) > 0 and stack[-1] == 'S':
            stack.pop()
        else:
            stack.append(c)
    return len(stack)

def printans(ans):    
    print(ans)

if __name__=='__main__':
    x=readinput()
    ans=main(x)
    printans(ans)
