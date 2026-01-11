from array import array

int_array = array('l',[0]*7)

print(len(int_array))

print('-' * 20)

int_array = array('i',[20,85,74,-99,108,7,-4,35])

print('-' * 20)

print(int_array)

print('-' * 20)

for i in int_array:
    print(i)


print('-' * 20)


print(f"1st--{int_array[0]}")
print(f"2st--{int_array[1]}")
print(f"3st--{int_array[2]}")
print(f"4st--{int_array[3]}")
print(f"5st--{int_array[4]}")
print(f"6st--{int_array[5]}")
print(f"7st--{int_array[6]}")
print(f"8st--{int_array[7]}")

print(int_array.itemsize)

print('-' * 20)


found_index = -1

for i in int_array:
    if int_array[(i)] == -99:
        found_index = index
        break

print(f"The value -99 was found at index {found_index}")