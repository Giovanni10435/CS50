def bubble(x):
    for i in range(len(x)):
        for j in range(0, len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x

x = [64, 34, 25, 12, 22, 11, 90]
frutas = ['banana', 'apple', 'cherry', 'pineapple', 'grape']

print("Original array:", x)
sorted_array = bubble(x)
print("Sorted array:", sorted_array)

print("Original array:", frutas)
sorted_frutas = bubble(frutas)
print("Sorted array:", sorted_frutas)

a = 3

print(a)