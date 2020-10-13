import time

print("Welcome To Squares!")
usernum = int(input("PLease Enter a Number: "))
rangenum = int(usernum + 1)
num1 = 1
if usernum >= 50 :
  print("PLease Enter A Smaller Number!")
else :
  for x in range(1, rangenum) :
    num2 = num1 * num1
    time.sleep(0.1)
    print(f"{num1} Squared = {num2} ")
    num1 = num1 + 1