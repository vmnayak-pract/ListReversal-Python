

def reverse_list(NumList, num):
    j = Number - 1
    i = 0
    while(i < j):
        temp = NumList[i]
        NumList[i] = NumList[j]
        NumList[j] = temp
        i = i + 1
        j = j - 1
    
NumList = []
N = int(input("Enter Total Number of List Elements: "))
for i in range(1, N + 1):
    value = int(input("Enter the Value of %d Element : " %i))
    NumList.append(value)
    
reverse_list(NumList, N)
print("\nThe Result of a Reverse List =  ", NumList)
