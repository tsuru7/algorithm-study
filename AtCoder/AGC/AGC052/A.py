def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    t=i_input()
    questions = []
    for _ in range(t):
        n = i_input()
        s1 = input()
        s2 = input()
        s3 = input()
        questions.append((n, s1, s2, s3))
    return t, questions

def main(t, questions):
    ans = []
    for n, s1, s2, s3 in questions:
        ans.append('0'*n+'1'*n+'0')
    return ans

def printans(ans):
    for a in ans:
        print(a)

if __name__=='__main__':
    t, questions=readinput()
    ans=main(t, questions)
    printans(ans)
