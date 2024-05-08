array= [45,65,75,15]
l= len(array)

for i in range(l):
    for j in range(0,l-i-1):

        if array[j]> array[j+1]:
            array[j], array[j+1]= array[j+1], array[j]


print("The sorted array is:", array)
        