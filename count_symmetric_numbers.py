
def sym(low,high):
    def num_len(n):
        return len(str(n))
    
    count = 0
    for n in range(low,high+1):
        if num_len(n)%2==0:
            s = str(n)
            mid = len(str(n))//2
            sumL = sum(int(digit) for digit in s[:mid])
            sumR = sum(int(digit) for digit in s[mid:])
            if sumL == sumR:
                count += 1
    return count