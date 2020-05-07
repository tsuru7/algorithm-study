def readinput():
    s = input().split()
    return s

def main(s):
    stack=[]
    ans = 0
    i = 0
    for c in s:
        if (c=='+'):
            op1 = int(stack.pop())
            op2 = int(stack.pop())
            stack.append(str(op1+op2))
        elif(c=='-'):
            op1 = int(stack.pop())
            op2 = int(stack.pop())
            stack.append(str(op2-op1))
        elif(c=='*'):
            op1 = int(stack.pop())
            op2 = int(stack.pop())
            stack.append(str(op1*op2))
        else:
            stack.append(c)
    ans = int(stack.pop())    
    return ans

if __name__=='__main__':
    s = readinput()
    ans = main(s)
    print(ans)

    