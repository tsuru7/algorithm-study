import sys
sys.setrecursionlimit(10**5)
INFTY = sys.maxsize
def i_input():
    return int(input())
def m_input():
    return map(int, input().split())
def l_input():
    return list(map(int, input().split()))

def readinput():
    n=i_input()
    skills = []
    for _ in range(n):
        skills.append(l_input())
    return n, skills

def print_bin(patterns):
    ans = []
    for pattern in patterns:
        ans.append(bin(pattern))
    print(ans)

def judge(x, skills):
    skill_patterns = set()
    for skill in skills:
        skill_pattern = 0
        for idx, v in enumerate(skill):
            if v >= x:
                skill_pattern |= 1<<idx
        skill_patterns.add(skill_pattern)
    skill_patterns_list = list(skill_patterns)
    # print_bin(skill_patterns_list)

    npatterns = len(skill_patterns_list)
    ans_pattern = 0
    for i in range(npatterns):
        pattern_i = skill_patterns_list[i]
        for j in range(i, npatterns):
            pattern_j = skill_patterns_list[j]
            for k in range(j, npatterns):
                pattern_k = skill_patterns_list[k]
                ans_pattern = pattern_i | pattern_j | pattern_k
                # print(i,j,k)
                # print(i,j,k,bin(ans_pattern))
                if ans_pattern == 2**5-1:
                    return True
    return False

def main(n,skills):
    # print(skills)
    ac = 0
    wa = 10**9+1
    while wa - ac > 1:
        wj = (ac+wa)//2
        # print()
        # print(ac, wj, wa)
        if judge(wj, skills):
            ac = wj
        else:
            wa = wj
    return ac

def printans(ans):
    print(ans)

if __name__=='__main__':
    n,skills=readinput()
    ans=main(n,skills)
    printans(ans)
