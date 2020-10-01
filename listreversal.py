n = int(input("Enter the number of items in List: "))
s = []

for i in range(n):
   lst = input("Enter list item value: ")
   s.append(lst)

print("The list is ", s)

i = 0
while i < len(s)/2:
   t = s[len(s)-1-i]
   s[len(s)-1-i] = s[i]
   s[i] = t
   i += 1
   
print("The reversed list is ", s)
