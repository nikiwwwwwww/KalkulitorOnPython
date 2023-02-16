mesycaVes = [31,28,31,30,31,30,31,31,30,31,30,31]
mesycaDef = [31,29,31,30,31,30,31,31,30,31,30,31]
mesyc = []
print("Введите год")
result = 0
god = int(input())
if((god % 4) == 0):
    mesyc = mesycaVes
else:
    mesyc = mesycaDef
for i in range(0,12):
    for j in range(1,mesyc[i]+1):
        if(j>9):
            while j > 0:
                result = result + (j % 10)
                j = j // 10
        else: result = result + j 
print(result)
