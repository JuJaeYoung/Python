count = 0
sum = 0
score = [9,41,12,3,74,15]

for i in range(6):
    sum += score[i]
    count += 1

print('합계:', sum)
print('평균:', sum / count)
