items=[]
comparison_counter=0

number_of_items=int(input("Enter the number of items to sort"))

for numbers in range(1,number_of_items+1):
  items.append(int(input("Enter a number to sort:")))

print("The unsorted list \n", items, "\n")

for i in range(len(items)):
  for j in range(len(items)-1-i):
   comparison_counter +=1
   if items[j]>items[j+1]:
     temp=items[j]
     items[j]=items[j+1]
     items[j+1]=temp
   
print('The sorted list\n', items)
print('\n It took', comparison_counter,'comparisons to sort the list.')