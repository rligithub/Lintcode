print('141 · Sqrt(x)')


def sqrt(self, x):
    start, end = 0, x
    while start +1 < end:
        mid = (end - start) //2 + start
        if mid*mid >= x:
            end = mid
        else:
            start = mid
    if end*end <=x:
        return end
    if start*start <x:
        return start

x=1
print(sqrt(0,x))

