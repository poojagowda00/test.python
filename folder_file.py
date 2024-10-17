import os
folders = input("Please provide the list of folders: ").split()

for folder in folders:
  try:
    files = os.listdir(folder)
  except FileNotFoundError:
    print("Please provide the vaild folder name, looks file the folder doesn't exits: " + folder)  
    continue

    print("====Listing the file" + folder)
  for file in files:
    print(file)

    
