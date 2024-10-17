import sys

type = sys.argv[1]

if type == "t2.micro":
  print("this is charge 2 dollars a day")

elif type == "t2.medium":  
  print("this is charge 4 dollars a day")

elif type == "t2.large":
  print("this is charge 8 dollars a day")

else:
  print("Please provide valid instance type")  