name1 = "Tien"
score1 = 10

name2 = "Bong"
score2 = 10

name3 = "Son"
score3 = 9

# print("{0:<10} {1:<5}".format("Tên","Số điểm"))
# print("{0:<10} {1:<5}".format(name1,score1))
# print("{0:<10} {1:<5}".format(name2,score2))
# print("{0:<10} {1:<5}".format(name3,score3))

# print(f"{'Tên' :<10} {'Số điểm' :<5}")
# print(f"{name1 :<10} {score1 :<5}")
# print(f"{name2 :<10} {score2 :<5}")
# print(f"{name3 :<10} {score3 :<5}")

print("%-10s  %-5s" % ("Tên", "Số điểm"))
print('%-10s  %-5d' % (name1, score1))
print('%-10s  %-5d' % (name2, score2))
print('%-10s  %-5d' % (name3, score3))