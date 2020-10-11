def readinput():
    h,w=map(int,input().split())
    slist = []
    for _ in range(h):
        slist.append(list(input()))
    return h,w,slist

def main(h,w,slist):
    count=0
    for x in range(w):
        for y in range(h):
            if (x+1 <= w-1) and (slist[y][x] == '.' and slist[y][x+1] == '.'):
                count += 1
                # print(x,y)
            if (y+1 <= h-1) and (slist[y][x] == '.' and slist[y+1][x] == '.'):
                count += 1
                # print(x,y)
    return count

if __name__=='__main__':
    h,w,slist=readinput()
    ans=main(h,w,slist)
    print(ans)
