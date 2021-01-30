#run code by entering "python3 witherror.py" in command line prompt

try:
  year = int(input("Enter year: "))
except:
  print("That is not a valid input")
  quit()

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
