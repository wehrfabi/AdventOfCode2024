
input = open("data.txt", "r")
sum = 0
list_1 = []
list_2 = []
while (True):
    line = input.readline()
    if not line:
        break
    x, y = line.split()
    list_1.append(x)
    list_2.append(y)
    list_1.sort()
    list_2.sort()
    sum = 0
    for i in range(len(list_1)):
        left = list_1[i]
        sum += int(left) * list_2.count(left)
print(sum)