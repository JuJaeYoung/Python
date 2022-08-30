a = [3,41,12,9,74,15]
max_a = 0
min_a = 0

for i in range(6):
    if i == 0:
        max_a = a[i]
        min_a = a[i]
    else:
        if max_a < a[i]:
            max_a = a[i]
            
        elif a[i] < min_a:
            min_a = a[i]

    
print('최댓값:',max_a,'\n최솟값:',min_a)

j = 0

while True:
    try:
        if j == 0:
            max_a = a[j]
            min_a = a[j]

        else:
            if max_a < a[j]:
                max_a = a[j]
                
            elif a[j] < min_a:
                min_a = a[j]
        j += 1
        
    except:
        break

print('최댓값:',max_a,'\n최솟값:',min_a)
