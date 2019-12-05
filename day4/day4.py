START = 168630
END = 718098

def meetit(x):
    st = str(x)
    if (st[5] >= st[4] >= st[3] >= st[2] >= st[1] >= st[0]):
        lastc = ''
        count = 0
        for c in st:
            if lastc == '' or lastc == c:
                count += 1
            if lastc != c and count == 2: # count > 2 for part1
                return True
                break
            elif lastc != c:
                count = 1
                lastc = c
        if count == 2: # cound >2 for part1
            return True
    return False

meets = 0
for x in range(START, END+1):
    if meetit(x):
        meets += 1

print(meets)

# Test Cases
#print(meetit(112233))
#print(meetit(123444))
#print(meetit(111122))
