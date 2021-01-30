#run code by entering "python3 nathan_liu_hw1.py" in command line prompt

year = int(input("Enter year: "))

if (year % 4) == 0:
  if (year % 100) == 0:
    if (year % 400) == 0:
      print(year,"is a leap year.")
    else:
      print(year,"is not a leap year.")
  else:
    print(year,"is a leap year.")
else:
  print(year,"is not a leap year.")