def transpose(list):
    result = []
    for i in range(len(list[0])):
        new = []
        for j in range(len(list)):
            new.append(list[j][i])
        result.append(new)

    return result

#main
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
list1 = []
i = 0
while (i < m):
    j = 0
    list1.append([])
    while j < n:
        v = int(input("matrix["+str(i)+","+str(j) +"]="))
        list1[i].append(v)
        j = j + 1
    i = i + 1
print(transpose(list1))
#########################################################
def sum_matrixes(list1, list2):
    result = []
    for i in range(len(list1)):
        sum = []
        for j in range(len(list1[i])):
            sum.append(list1[i][j] + list2[i][j])
        result.append(sum)
    return result

#main
m = int(input("Enter the number of rows for list1: "))
n = int(input("Enter the number of columns for list1: "))
list1 = []
i = 0
while (i < m):
    j = 0
    list1.append([])
    while j < n:
        v = int(input("matrix["+str(i)+","+str(j) +"]="))
        list1[i].append(v)
        j = j + 1
    i = i + 1

m = int(input("Enter the number of rows for list2: "))
n = int(input("Enter the number of columns for list2: "))
list2 = []
i = 0
while (i < m):
    j = 0
    list2.append([])
    while j < n:
        v = int(input("matrix["+str(i)+","+str(j) +"]="))
        list2[i].append(v)
        j = j + 1
    i = i + 1

print(sum_matrixes(list1, list2))
#########################################################
def product_matrixes(list1, list2):
    result = []
    for i in range(len(list1)):
        new = []
        for j in range(len(list2[0])):
            new.append(0)
        result.append(new)
        
    for i in range(len(list1)):
        for j in range(len(list2[0])):
            for n in range(len(list2)):
                result[i][j] += list1[i][n] * list2[n][j]

    finish = []
    for i in result:
        finish.append(i)

    return finish

#main

m = int(input("Enter the number of rows for list1: "))
n = int(input("Enter the number of columns for list1: "))
list1 = []
i = 0
while (i < m):
    j = 0
    list1.append([])
    while j < n:
        v = int(input("matrix["+str(i)+","+str(j) +"]="))
        list1[i].append(v)
        j = j + 1
    i = i + 1

m = int(input("Enter the number of rows for list2: "))
n = int(input("Enter the number of columns for list2: "))
list2 = []
i = 0
while (i < m):
    j = 0
    list2.append([])
    while j < n:
        v = int(input("matrix["+str(i)+","+str(j) +"]="))
        list2[i].append(v)
        j = j + 1
    i = i + 1

print(product_matrixes(list1, list2))
