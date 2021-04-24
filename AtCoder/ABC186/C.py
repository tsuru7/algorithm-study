def readinput():
    n=int(input())
    return n

def any_num8(m):
    if m==1:
        return [0, 1, 2, 3, 4, 5, 6, 7]

    ans_list=[]
    temp_list = any_num8(m-1)
    for i in range(8):
        for temp in temp_list:
            ans_list.append(i*8**(m-1)+temp)
    return ans_list

def seven_nums8(m, n):
    if m==1:
        return [7] if n >= 7 else []

    ans_list=[]
    # case1
    anynums=any_num8(m-1)
    for num in anynums:
        x = 7*8**(m-1)+num
        if x <= n:
            ans_list.append(x)
    
    # case2
    sevennums=seven_nums8(m-1, n)
    for num in sevennums:
        for d in (0, 1, 2, 3, 4, 5, 6):
            x = d*8**(m-1)+num
            if x <=n:
                ans_list.append(x)
    
    return ans_list

def any_num10(m):
    if m==1:
        return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    ans_list=[]
    temp_list = any_num10(m-1)
    for i in range(10):
        for temp in temp_list:
            ans_list.append(i*10**(m-1)+temp)
    # print(ans_list)
    return ans_list

def seven_nums10(m, n):
    if m==1:
        return [7] if n >= 7 else []

    ans_list=[]
    # case1
    anynums=any_num10(m-1)
    for num in anynums:
        x = 7*10**(m-1)+num
        if x <= n:
            ans_list.append(x)
    
    # case2
    sevennums=seven_nums10(m-1, n)
    for num in sevennums:
        for d in (0, 1, 2, 3, 4, 5, 6, 8, 9):
            x = d*10**(m-1)+num
            if x <=n:
                ans_list.append(x)
    
    return ans_list
    

def main(n):
    sevennums10 = seven_nums10(5, n)
    sevennums8 = seven_nums8(6, n)
    set10 = set(sevennums10)
    set8 = set(sevennums8)
    inter = set10 & set8

    # print(sevennums10)
    # print(sevennums8)
    # print(inter)
    return  n - len(sevennums10) - len(sevennums8) + len(inter)



    ans=0
    return ans

if __name__=='__main__':
    n=readinput()
    ans=main(n)
    print(ans)
