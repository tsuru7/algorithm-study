def main():
    s = input()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if len(s) < 26:
        for c in alphabet:
            if c in s:
                continue
            else:
                return s+c
    else:
        for i in range(25, 0, -1):
            if s[i-1] < s[i]:
                for c in sorted(s[i:]):
                    if c > s[i-1]:
                        return s[:i-1]+c
        else:
            return -1

if __name__ == '__main__':
    ans = main()
    print(ans)
