def readinput():
    h,w=map(int,input().split())
    smap=[]
    for _ in range(h):
        smap.append(input())
    return h,w,smap

def main(h,w,smap):
    # print(smap)
    total_count = 0
    for i in range(h-1):
        for j in range(w-1):
            count = 0
            if smap[i][j] == '#':
                count += 1
            if smap[i][j+1] == '#':
                count += 1
            if smap[i+1][j+1] == '#':
                count += 1
            if smap[i+1][j] == '#':
                count += 1
            if count == 1 or count == 3:
                total_count += 1
    return total_count

def printans(ans):
    print(ans)

if __name__=='__main__':
    h,w,smap=readinput()
    ans=main(h,w,smap)
    printans(ans)
