
def sym(low,high):
    count = 0
    for n in range(low,high+1):
        if len(str(n))%2==0:
            sumL = sum(int(digit) for digit in str(n)[:len(str(n))//2])
            sumR = sum(int(digit) for digit in str(n)[len(str(n))//2:])
            if sumL == sumR:
                count += 1
    return count

print(sym(1,100))