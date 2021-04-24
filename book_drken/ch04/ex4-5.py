def main(k):
    keta = len(str(k))
    return num753('', k, keta)

def num753(s, x, k):
    if k==0:
        if '3' in s and '5' in s and '7' in s and int(s) <= x:
            return 1
        else:
            return 0
    ans = 0
    ans += num753('', x, k-1) if s == '' else 0
    ans += num753(s+'3', x, k-1)
    ans += num753(s+'5', x, k-1)
    ans += num753(s+'7', x, k-1)
    return ans           

        


if __name__ == '__main__':
    n=int(input())
    print(main(n))
