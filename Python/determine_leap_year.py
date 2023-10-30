year=int(input("Nhập năm: "))

if year%4==0:
  if year%100==0 and not year%400==0:
    print("Năm", year, "không phải là năm nhuận!")
  else:
    print("Năm", year, "là năm nhuận!")
else:
  print("Năm", year, "không phải là năm nhuận!")
