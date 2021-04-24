def readinput():
    s=input()
    return s

def main(s):

    multiples_ = [
    '8', '16', '32', '48', '56', '64', '72', '88', '96', '112', '128', '136', '144', '152', '168', '176', '184', '192',
         '216', '232', '248', '256', '264', '272', '288', '296', '312', '328', '336', '344', '352', '368', '376', '384', '392',
         '416', '432', '448', '456', '464', '472', '488', '496', '512', '528', '536', '544', '552', '568', '576', '584', '592',
         '616', '632', '648', '656', '664', '672', '688', '696', '712', '728', '736', '744', '752', '768', '776', '784', '792',
         '816', '832', '848', '856', '864', '872', '888', '896', '912', '928', '936', '944', '952', '968', '976', '984', '992',
    ]

    sorted_multiples_ = []
    for multi in multiples_:
        sorted_multiples_.append(''.join(sorted(multi)))

    # print(sorted_multiples_)

    if len(s) <= 3:
        if ''.join(sorted(s)) in sorted_multiples_:
            return 'Yes'
        else:
            return 'No'

    multiples = []
    n = 8
    while n < 1000:
        nstr = '{:03d}'.format(n)
        if '0' in nstr:
            n += 8
            continue
        # nstr = str(n)
        digits = [0]*10
        for c in nstr:
            i = int(c)
            digits[i] += 1
        multiples.append(digits)
        n += 8
    
    digit_table = [0]*10
    # for c in '{:03d}'.format(int(s)):
    for c in s:
        i = int(c)
        digit_table[i] += 1

    for multiple in multiples:
        # multiple_flag = False
        for i in range(1, 10):
            if digit_table[i] < multiple[i]:
                break
        else:
            # multiple_flag = True
            return 'Yes'
    return 'No'

if __name__=='__main__':
    s=readinput()
    ans=main(s)
    print(ans)
