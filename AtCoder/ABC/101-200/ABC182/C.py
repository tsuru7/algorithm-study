def readinput():
    n=int(input())
    return n

def main(n):
    list_n = list(str(n))

    count1=0
    count2=0
    sum=0
    for c in list_n:
        if c in ('1', '4', '7'):
            count1+=1
        elif c in ('2', '5', '8'):
            count2+=2
        sum += int(c)

    if sum < 3:
        return -1

    res = sum % 3

    if res == 0:
        return 0
    elif res == 1:
        if count1 >= 1 :
            return 1 if len(list_n) > 1 else -1
        elif count2 >= 2:
            return 2 if len(list_n) > 2 else -1
        else:
            return -1
    else:
        if count2 >= 1 :
            return 1 if len(list_n) > 1 else -1
        elif count1 >= 2:
            return 2 if len(list_n) > 2 else -1
        else:
            return -1

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
