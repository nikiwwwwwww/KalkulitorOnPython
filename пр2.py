mesyca = [31,28,31,30,31,30,31,31,30,31,30,31]
print("Введите год")
result = 0
god = int(input())
if god % 4 != 0:
    mesyca[1] = 28
elif god % 100 == 0:
    if god % 400 == 0:
        mesyca[1] = 29
    else:
        mesyca[1] = 28
else:
    mesyca[1] = 29
for i in range(0,12):
    for j in range(1,mesyca[i]+1):
        if(j>9):
            while j > 0:
                result = result + (j % 10)
                j = j // 10
        else: result = result + j 
print(result)
