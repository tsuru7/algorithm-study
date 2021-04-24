from collections import deque
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    s=input()
    return n,s

def main(n,s):
    stack = deque()
    for c in s:
        stack.append(c)
        if len(stack) >= 3:
            temp = stack[-3]+stack[-2]+stack[-1]
            if temp == 'fox':
                for _ in range(3):
                    stack.pop()
    
    return len(stack)

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,s=readinput()
    ans=main(n,s)
    printans(ans)
