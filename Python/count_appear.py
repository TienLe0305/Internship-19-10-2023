numbers = [1, 3, 2, 4, 5, 2, 3, 6, 7, 5, 8, 1, 2,
           2, 4, 9, 3, 4, 3, 4, 5, 1, 2, 3, 2, 2, 2, 3, 4]
i = int(input())

count = numbers.count(i)
times = ["zero", "one", "two", "three", "four",
         "five", "six", "seven", "eight", "nine", "ten"]

print("Number", i, "appear " + times[count] + " time in the list!")
