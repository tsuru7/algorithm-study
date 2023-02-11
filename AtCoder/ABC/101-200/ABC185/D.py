def readinput():
    n,m=map(int,input().split())
    if m > 0:
        a=list(map(int,input().split()))
    else:
        a = []
    return n,m,a

def main(n,m,a):
    white_list = []
    a_sorted = sorted(a)
    w0 = 1
    b0 = 0
    min_white = n
    for b in a_sorted:
        if b == b0 + 1:
            b0 += 1
            w0 += 1
        else:
            white_list.append(b-w0)
            min_white = min(min_white, b-w0)
            w0 = b + 1
            b0 = b
            # print(white_list)
    else:
        if w0 <= n:
            # print(w0, n)
            white_list.append(n-w0+1)
            min_white = min(min_white, n-w0+1)
            # print(white_list, min_white)


    k = min_white
    # print(white_list, k)

    count=0
    for white in white_list:
        count += white // k
        # print(count)
        if white % k != 0:
            count +=1
            # print(count)

    return count

if __name__=='__main__':
    n,m,a=readinput()
    ans=main(n,m,a)
    print(ans)
