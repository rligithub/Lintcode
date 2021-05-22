
def selectionsort(a):
    mini = 0
    for i in range(len(a)):
        mini = i
        for j in range(i+1,len(a)):
            if a[j] < a[mini]:
                mini = j

        a[mini], a[i] = a[i], a[mini]
    return a



a = [5,6,7,2,1,0]
print(selectionsort(a))