even = []
odd = []
count_1 = 0
count_2 = 0
n1 = int(input("Enter a value 1: "))
n2 = int(input("Enter a value 2: "))
n3 = int(input("Enter a value 3: "))
n4 = int(input("Enter a value 4: "))
n5 = int(input("Enter a value 5: "))
num_list = [n1,n2,n3,n4,n5]
for i in num_list:
    if i%2 == 0:
        count_1 = count_1 + 1
        even.append(i)
    else:
        count_2 = count_2 + 1
        odd.append(i)
print("The give list is :", num_list)
print("Number of even num :", count_1)
print(even)
print("Number of odd num :", count_2)
print(odd)
