my_list = [8.5, 5.6, 6.7, 7.8, 8.4, 4.9, 9.0, 0.5, -1.2, -8.9]
max = max(my_list)
min = min(my_list)

a = float(input())
b = float(input())

if (a <= min) and (b >= max):
    print("All elements in list belong to [" + str(a) + "," + str(b) + "]")
elif (b < min) or (a > max):
    print(
        "All elements in list do not belong to [" + str(a) + "," + str(b) + "]")
else:
    print(
        "Some elements in list do not belong to [" + str(a) + "," + str(b) + "]")
